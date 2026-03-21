from django.contrib import admin
from apps.projects.models import (
    Category,ProjectSection,Projects
)

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    
@admin.register(ProjectSection)
class ProjectTitleAdmin(admin.ModelAdmin):
    list_display = ('id','title','subtitle')
    search_fields = ('title',)
    
    def has_add_permission(self, request):
        return not ProjectSection.objects.exists()
    
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_filter = ['category']
    search_fields = ('name',)
    autocomplete_fields = ['category']