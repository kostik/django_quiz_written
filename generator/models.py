import json

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from quiz.models import Quiz


@python_2_unicode_compatible
class WrittenQuiz(models.Model):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=60, blank=False)

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True, help_text=_("a description of the quiz"))

    quizzes = models.ManyToManyField(Quiz)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        super(WrittenQuiz, self).save(force_insert, force_update, *args, **kwargs)

    class Meta:
        verbose_name = _("Written Quiz")
        verbose_name_plural = _("Written Quizzes")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class WrittenQuizExam(models.Model):
    class Meta:
        permissions = (
            ('can_see_answers', 'Can see answers'),
        )

    description = models.CharField(
        max_length=100,
        verbose_name=_("Description"),
        blank=True, help_text=_("a description of the exam"))

    timestamp = models.DateTimeField(
        verbose_name=_("Created"),
        auto_now_add=True)

    written_quiz = models.ForeignKey(WrittenQuiz)

    question_list = models.CharField(
        max_length=1024, verbose_name=_("Question List")
    )

    def __str__(self):
        return "%s @ %s" % (self.description, self.timestamp)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        super(WrittenQuizExam, self).save(force_insert, force_update, *args, **kwargs)

    def clean(self):
        data = {}
        for quiz in self.written_quiz.quizzes.all():
            if quiz.random_order is True:
                question_set = quiz.question_set.all() \
                    .select_subclasses() \
                    .order_by('?')
            else:
                question_set = quiz.question_set.all() \
                    .select_subclasses()

            question_set = [item.id for item in question_set]

            if quiz.max_questions and quiz.max_questions < len(question_set):
                question_set = question_set[:quiz.max_questions]

            if question_set:
                data[quiz.id] = question_set

        if data:
            self.question_list = json.dumps(data)
        else:
            raise ValidationError(_('This test is empty'))
