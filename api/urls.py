from django.urls import path
from . import views
# from .views import test_mysql_connection


urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('test-mysql/', views.test_mysql_connection, name='test_mysql_connection'),
]
