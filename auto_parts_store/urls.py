from django.urls import path
from . import views

urlpatterns = [
    path('avtoparts_list/', views.avtopartsListView, name='AvtopartsList'),
    path('avtoparts_detail/<int:id>/', views.avtopartsDetailView, name='detail'),
    path('avtoparts_detail/<int:id>/delete/', views.deleteProductsView, name='delete'),
    path('avtoparts_detail/<int:id>/update/', views.updateProductsView, name='update'),
    path('create_product/', views.createProductsView, name='createProduct'),
]