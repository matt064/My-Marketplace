from django.urls import path

from . import views


app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('<int:pk>/', views.detail, name='details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit_item, name='edit'),
    path('new/', views.new_item, name='new'),
]