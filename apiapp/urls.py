from django.urls import path
from . import views

urlpatterns = [
  path('', views.CommentListView.as_view()),
  path('<int:id>/', views.CommentListView.as_view()),
]