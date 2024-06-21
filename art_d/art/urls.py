from django.urls import path
from . import views


app_name = 'art'


urlpatterns = [
    path('', views.home, name='home'),
    path('art/<slug:slug>/', views.art_details, name='art-details'),
    
    
    
    
    path('cart/', views.cartpage, name='cart'),
    path('checkout/', views.checkoutpage, name='checkout'),
    path('product_details/', views.product_details, name="product_details" ),
    path('shop/', views.shop, name='shop'),
    
    path('favorite/', views.favorite, name='favorite'),
    
   
]