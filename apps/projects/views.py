from django.shortcuts import render
from apps.projects.models import (
    Category, ProjectSection, Projects
)

# Create your views here.

# Project display and filtering logic is implemented in:
# apps.projects.templatetags.project_tags.py