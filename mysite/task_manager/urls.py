from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeTasks.as_view(), name='home'),
    path('search', SearchTasks.as_view(), name='search'),
    path('filter/', FilterTasks.as_view(), name='filter'),
    path('task/<int:pk>/', ViewTasks.as_view(), name='view_tasks'),
    #path('task/<int:pk>/', Tasks.as_t(), name='view_tasks'),
]
