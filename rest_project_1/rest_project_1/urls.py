from django.contrib import admin
from django.urls import path
from women.views import WomenAPIView, WomenListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/womenlist/', WomenAPIView.as_view()),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIView.as_view()),
    path('api/v1/womenlist/', WomenListAPIView.as_view()),
    path('api/v1/womenlist/<int:pk>/', WomenListAPIView.as_view()),
]