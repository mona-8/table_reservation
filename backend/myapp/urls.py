from django.urls import path
from .views import RestaurantView, postData

urlpatterns = [
    path("data/", RestaurantView.as_view(), name="res_view"),
    path("addInfo/", postData, name="add_info")
]