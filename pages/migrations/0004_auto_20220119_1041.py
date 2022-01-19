# Generated by Django 3.2.9 on 2022-01-19 09:41

from django.db import migrations
import polls.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20220118_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='poll',
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='text',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('poll', wagtail.core.blocks.StructBlock([('poll', wagtail.snippets.blocks.SnippetChooserBlock(polls.models.Question))]))], default=None),
        ),
    ]
