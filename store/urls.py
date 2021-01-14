from django.urls import path,include
from .views import cart,checkout,store
urlpatterns = [
    path('',store,name='store'),
    path('cart/',cart,name='cart'),
    path('checkout/',checkout,name='checkout'),
]
