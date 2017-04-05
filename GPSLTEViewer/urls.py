from django.conf.urls import url
from django.conf.urls import include
from GPSLTEViewer import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]