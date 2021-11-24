from django.urls import path
from . import views

app_name = 'orders'


urlpatterns = [
    path('orderitem/', views.OrderItemList.as_view()),
    path('orderitem/<int:pk>/', views.OrderItemDetail.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>/', views.OrderDetail.as_view()),
    path('products/', views.ProductListView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view()),
]
