from django.db import models
from django.contrib.auth.models import AbstractUser
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class AuthorProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=250)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('bio'),
        ImageChooserPanel('photo')
    ]

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    profile = models.OneToOneField(AuthorProfile, on_delete=models.CASCADE, null=True)