from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register('tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'menu/items/',
        views.MenuItemsView.as_view(),
        name='menu-items'
    ),
    path(
        'menu/items/<int:pk>/',
        views.SingleMenuItemView.as_view(),
        name='single-menu-item'
    ),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]