from cataract import views
from django.urls import path

urlpatterns = [
    path('', views.cataractImageUpload, name = 'upload_image'),
]