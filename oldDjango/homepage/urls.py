from django.conf.urls import url
from homepage import views

urlpatterns = [
    url('^$', views.home, name='home_page'),
]
