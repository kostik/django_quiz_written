# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='WrittenQuiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('description', models.TextField(help_text='a description of the quiz', verbose_name='Description', blank=True)),
                ('quizzes', models.ManyToManyField(to='quiz.Quiz')),
            ],
            options={
                'verbose_name': 'Written Quiz',
                'verbose_name_plural': 'Written Quizzes',
            },
        ),
    ]
