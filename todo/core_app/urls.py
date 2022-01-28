from django.urls import path 
# from core_app.views import test_api
# from . import views
from core_app.views import (
    ChecklistsAPIViews, 
    ChecklistAPIViews,
    ChecklistItemCreateAPIViews,
    ChecklistItemAPIViews
)

urlpatterns = [
    path('api/checklists/', ChecklistsAPIViews.as_view()),
    path('api/checklist/<int:pk>/', ChecklistAPIViews.as_view()),
    path('api/checklistItem/create/', ChecklistItemCreateAPIViews.as_view()),
    path('api/checklistItem/<int:pk>/', ChecklistItemAPIViews.as_view()),
]
