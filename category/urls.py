from django.urls import path
from . import views

app_name = 'category'
urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_add, name='category_add'),
    path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('import', views.import_category, name='import_category'),
    path('export', views.export_category, name='export_category'),
]
