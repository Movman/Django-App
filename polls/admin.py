from django.contrib import admin
from .models import Question, Choice
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Question, Choice
# Register your models here.
class Choiceline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [Choiceline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)



# WAGTAIL ADMIN SECTION
class PollsAdmin(ModelAdmin):
    model = Question
    menu_label = "Polls"
    menu_icon = "placeholder"
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("question_text", "pub_date",)
    list_filter = ('question_text',)
    search_fields = ("question_text",)

modeladmin_register(PollsAdmin)
