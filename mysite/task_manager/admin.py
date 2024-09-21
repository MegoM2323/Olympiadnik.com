from django.contrib import admin
from .models import Tasks#, Category


class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'themes')
    list_display_links = ("id", "title")
    search_fields = ('title', 'content')
    list_filter = ('themes',)


#class CategoryAdmin(admin.ModelAdmin):
#    list_display = ('id', 'title')
#    list_display_links = ("id", "title")
#    search_fields = ('title',)


admin.site.register(Tasks, TasksAdmin)
#admin.site.register(Category, CategoryAdmin)
