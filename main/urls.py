from django.conf.urls import url
from main import views

urlpatterns = [
    url('list/', views.main_list),
    url('exception/', views.main_exception)
]