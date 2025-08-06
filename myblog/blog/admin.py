from django.contrib import admin
from .models import Post, Category, Subcategory
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("NTA Dashboard")
admin.site.site_title = _("MySite Admin Portal")
admin.site.index_title = _("Welcome to MySite Admin")   


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Post)




