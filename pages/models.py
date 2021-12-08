from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.


class BlogPage(Page):
    body = RichTextField()

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]