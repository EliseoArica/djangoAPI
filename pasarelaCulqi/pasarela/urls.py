from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/pagos/$', views.pago_list),
]
