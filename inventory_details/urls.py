from django.conf.urls import url
from inventory_details import views

urlpatterns = [
    url(r'list', views.ListInventoyry.as_view()),
    url(r'purchase', views.PurchaseView.as_view())
]
