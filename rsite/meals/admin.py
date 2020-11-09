from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import *

# Register your models here.

# Apply summernote to all TextField in model.
class MealsAdmin(SummernoteModelAdmin , admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display      = ['name' , 'price' , 'preparation_time','people']
    search_fields     = ['name' , 'description']
    list_filter       = ('category','people',)

admin.site.register(Meals , MealsAdmin)
admin.site.register(Category)
