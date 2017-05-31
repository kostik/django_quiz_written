from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required

from .views import WrittenQuizExamDetailView

urlpatterns = patterns('',

                       url(regex=r'^(?P<pk>[\d.]+)/take/$',
                           view=WrittenQuizExamDetailView.as_view(),
                           name='written_quiz_exam_take'),

                       url(regex=r'^(?P<pk>[\d.]+)/answers/$',
                           view=permission_required('', login_url='login')(WrittenQuizExamDetailView.as_view()),

                           name='written_quiz_exam_answers',
                           kwargs={"answers": True}
                       )
                       )
