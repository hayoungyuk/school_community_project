from django.contrib import admin
from .models import Schoolapp, Tag

# Register your models here.
admin.site.register(Schoolapp)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Tag,TagAdmin)