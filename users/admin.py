from .models import AuthorProfile
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

class AuthorProfileAdmin(ModelAdmin):
    model = AuthorProfile
    menu_label = "Author"
    menu_icon = "placeholder"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "bio",)
    list_filter = ('name',)
    search_fields = ("name",)

modeladmin_register(AuthorProfileAdmin)