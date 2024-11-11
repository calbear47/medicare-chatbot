from django.urls import path
from . import views

urlpatterns = [
    path('query/', views.query_plans, name='query_plans'),
    path('upload-pdf/', views.upload_pdf, name='upload_pdf'),
    path('health/', views.health_check, name='health_check'),
]