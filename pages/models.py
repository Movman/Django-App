from django.db import models
from django.conf import settings
from wagtail.search import index

from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from wagtail.images.blocks import ImageChooserBlock

from polls.models import Question
from polls import blocks_polls

# Create your models here.

class IndexPage(Page):
    body = RichTextField(default=None)

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]


class BlogPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # pouzivame blocky, nie panels
    # stream field je list tupples: ('nazov_objektu', Block)
    text = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('poll', blocks_polls.PollsBlock()),
    ], default=None)


    # Editor panels configuration - tu pouzivame panels
    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        StreamFieldPanel('text'),
        FieldPanel('owner'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('title'),
]


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=400)
