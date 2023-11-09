from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductView.as_view()),
    path('order/', views.OrderCLView.as_view()),
    path('summer_products/', views.ProductSummerView.as_view()),
    path('autumn_products/', views.ProductAutumnView.as_view()),
    path('winter_products/', views.ProductWinterView.as_view()),
    path('spring_products/', views.ProductSpringView.as_view()),
    path('products/<int:id>/', views.ProductDetailView.as_view()),
]