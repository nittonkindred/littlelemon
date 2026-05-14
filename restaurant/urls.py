
from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.BookingView.as_view(), name='bookings'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu'),
]