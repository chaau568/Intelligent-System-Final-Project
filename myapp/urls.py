from django.urls import path #type: ignore
from . import views  
from django.conf import settings #type: ignore
from django.conf.urls.static import static #type: ignore

urlpatterns = [
  path('', views.home, name='home'),
  path('emotion_details/', views.emotion_details, name='emotion_details'),
  path('emotion_model/', views.emotion_model, name='emotion_model'),
  path('show_result/', views.show_result, name='show_result'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)