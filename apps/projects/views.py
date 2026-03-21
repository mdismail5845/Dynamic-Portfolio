from django.shortcuts import render
from apps.projects.models import (
    Category, ProjectSection, Projects
)

# Create your views here.
# def projects(request):
#     categories = Category.objects.all()
#     project_section = ProjectSection.objects.first()
#     category_id = request.GET.get('category')
#     if not category_id or category_id == 'all':
#         projects = Projects.objects.select_related('category').all()
#     else:
#         projects = Projects.objects.filter(category_id = category_id)
#     context = {
#         'categories' : categories,
#         'project_section' : project_section,
#         'projects' : projects,
#         'active_category' : category_id,
#     }
#     return render(request, 'projects.html', context)