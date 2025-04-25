from django.urls import path
from . import views

urlpatterns = [
    path('workspaces/', views.workspace_list, name='workspace_list'),
    path('workspaces/create/', views.workspace_create, name='workspace_create'),
    path('workspaces/<int:workspace_id>/', views.page_list, name='page_list'),
    path('workspaces/<int:workspace_id>/create-page/', views.page_create, name='page_create'),
    path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
]