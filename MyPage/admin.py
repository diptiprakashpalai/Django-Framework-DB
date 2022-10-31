from django.contrib import admin

# Register your models here.
from .models import book

class bookAdmin(admin.ModelAdmin):
     list_filter = ("title", "author", "rating")
     list_display = ("title", "author", "rating")
       
admin.site.register(book, bookAdmin)
