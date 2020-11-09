from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import *

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin , admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display      = ['title' , 'author' , 'category' , 'created']
    search_fields     = ['title' , 'content']
    list_filter       = ('category','tags',)

admin.site.register(Post , PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
