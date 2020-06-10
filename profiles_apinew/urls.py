from django.urls import path

from profiles_apinew import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
