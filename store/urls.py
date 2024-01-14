from django.urls import path
from . import views # the . here means from this directory

urlpatterns=[
    path('',views.store, name='store'), #here we wanna make 'store' our home page so that is why we dont give a path as 1st argument
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

]