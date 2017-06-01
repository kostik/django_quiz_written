# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_writtenquizexam'),
    ]

    operations = [
        migrations.AddField(
            model_name='writtenquizexam',
            name='question_list',
            field=models.CommaSeparatedIntegerField(default=[], max_length=1024, verbose_name='Question List'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='writtenquizexam',
            name='description',
            field=models.CharField(help_text='a description of the exam', max_length=100, verbose_name='Description', blank=True),
        ),
    ]
