from django import template
from apps.projects.models import (
    Category, ProjectSection, Projects
)

register = template.Library()

@register.inclusion_tag("projects.html", takes_context=True)
def show_projects(context, category_id=None):
    categories = Category.objects.all()
    project_section = ProjectSection.objects.first()
    if category_id is None:
        category_id = context['request'].GET.get('category','all')
    if not category_id or category_id == 'all':
        projects = Projects.objects.select_related('category').all()
    else:
        projects = Projects.objects.filter(category_id = category_id)
    return {
        'categories' : categories,
        'project_section' : project_section,
        'projects' : projects,
        'active_category' : category_id,
    }