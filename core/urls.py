from django.urls import path
from .views import home, projects, project_detail, skills, contact

urlpatterns = [
    path('', home),
    path('projects/', projects),
    path('project/<int:id>/', project_detail),
    path('skills/', skills),
    path('contact/', contact),
]
