# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WrittenQuizExam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(help_text='a description of the quiz', verbose_name='Description', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('written_quiz', models.ForeignKey(to='generator.WrittenQuiz')),
            ],
        ),
    ]
