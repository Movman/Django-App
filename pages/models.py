from django.db import models
from django.db.models.fields.files import ImageField

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from wagtail.images.blocks import ImageChooserBlock

# Create your models here.

class IndexPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]



class BlogPage(Page):
    image = ImageField(blank=True, default=None)
    author = models.CharField(max_length=200, default=None)
    date = models.DateField("Post date", default=None)
    text = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], default=None)

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('text'),
    ]

class ContactPage(Page):
    message = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("message")
    ]