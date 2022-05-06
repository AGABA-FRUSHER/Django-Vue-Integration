from django.urls import path
from .views import Tasks
from .import views


urlpatterns =[
    path('tasks/', views.tasks),
    path('tasks/<int:pk>', views.task_detail)
]