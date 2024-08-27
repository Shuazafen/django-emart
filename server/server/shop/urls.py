from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name="home page"),
    path('detail/<str:model_name>/<int:pk>', views.detail, name="detail"),
    path('order.html', views.order, name='order' )
]