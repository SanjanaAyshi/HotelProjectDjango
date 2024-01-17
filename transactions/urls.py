from django.urls import path
from .views import addMoney,BookingView

urlpatterns = [
    path("deposit/", addMoney, name="addMoney"),
    path("Booked/<int:id>", BookingView.as_view(), name="Booked"),
]
