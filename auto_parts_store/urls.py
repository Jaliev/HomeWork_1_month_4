from django.urls import path
from . import views

urlpatterns = [
    path('avtoparts_list/', views.avtopartsListView, name='AvtopartsList'),
    path('avtoparts_detail/<int:id>/', views.avtopartsDetailView, name='detail'),
]