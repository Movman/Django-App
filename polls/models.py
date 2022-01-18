import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel

from wagtail.core.models import Page, Orderable
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


@register_snippet
class Question(ClusterableModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    panels = [
        FieldPanel('question_text'),
        FieldPanel('pub_date'),
        InlinePanel('choices', label="Choices"),
    ]

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(Orderable):
    question = ParentalKey(Question, on_delete = models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    panels = [
        FieldPanel('choice_text'),
        FieldPanel('votes')
    ]

    def __str__(self):
        return self.choice_text
