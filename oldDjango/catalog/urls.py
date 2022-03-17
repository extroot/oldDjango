from django.conf.urls import url
from catalog import views

urlpatterns = [
    url(r'\d{1,10}/', views.item_detail, name='product_page'),
    url('', views.item_list, name='all_products'),
]