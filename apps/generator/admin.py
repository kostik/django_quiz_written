from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from .models import WrittenQuiz, WrittenQuizExam


class WritttenQuizExamAdmin(admin.TabularInline):
    model = WrittenQuizExam
    fields = ("description", "exam_link", "answers_link")
    readonly_fields = ('exam_link','answers_link')

    def exam_link(self, object):

        if object.pk:
            url = reverse("written_quiz_exam_take", args=(object.pk,))
            return "<a href={url}>".format(url=url) + _("link") + "</a>"
        else:
            return ""

    def answers_link(self, object):

        if object.pk:
            url = reverse("written_quiz_exam_answers", args=(object.pk,))
            return "<a href={url}>".format(url=url) + _("link") + "</a>"
        else:
            return ""

    answers_link.allow_tags = True
    exam_link.allow_tags = True


    # disable delete action
    # todo: restore it!
    # def has_delete_permission(self, request, obj=None):
    #    return False


class WrittenQuizAdmin(admin.ModelAdmin):
    inlines = [WritttenQuizExamAdmin]

    # def get_quizzes(self, request, queryset):
    #     message = ''
    #     for written_quiz in queryset:
    #
    #         for quiz in written_quiz.quizzes.all():
    #             for question in quiz.question_set.all().select_subclasses():
    #                 message += str(question)
    #
    #     level = messages.SUCCESS
    #     self.message_user(request, message, level)
    #
    # get_quizzes.short_description = "Show questions"
    #
    # actions = ['get_quizzes']


admin.site.register(WrittenQuiz, WrittenQuizAdmin)
