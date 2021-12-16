from django.db import models
from django.db.models.fields import TextField
from wagtail.search import index

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from wagtail.images.blocks import ImageChooserBlock

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
    text = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], default=None)

    # Editor panels configuration

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        StreamFieldPanel('text'),
    ]

    search_fields = Page.search_fields + [
    index.SearchField('title'),
]


class ContactPage(Page):
    pass


class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email