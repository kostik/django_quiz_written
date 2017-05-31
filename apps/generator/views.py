import json

from django.forms import RadioSelect, forms
from django.views.generic import DetailView

from quiz.models import Question, Quiz
from .models import WrittenQuizExam


class WrittenQuizExamDetailView(DetailView):
    model = WrittenQuizExam

    def get_context_data(self, **kwargs):
        context = super(WrittenQuizExamDetailView, self).get_context_data(**kwargs)
        obj = self.get_object()

        questions_dict = json.loads(obj.question_list)
        quizzes = {}

        for quiz_id, question_list in questions_dict.iteritems():
            questions = []
            for question_id in question_list:
                question = Question.objects.get_subclass(id=question_id)
                question.class_name = str(question.__class__)
                questions.append(question)

            quizzes[Quiz.objects.get(id=quiz_id)] = questions

        context['quizzes'] = quizzes

        return context
