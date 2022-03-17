from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^users/\d{1,10}/', views.user_detail, name='user_page'),
    url('signup/', views.signup, name='signup'),
    url('profile/', views.profile, name='profile_page'),
    url('users/', views.user_list, name='users_page'),
]
