from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
from api import views
router=DefaultRouter()
router.register("accounts/users",views.UsersView,basename="users")
router.register("accounts/owners",views.OwnersView,basename="owners")
router.register("users/profile",views.ProfileView,basename="profile")

router.register("places",views.Placeview,basename="places")
router.register("hotels",views.HotelView,basename="hotels")
router.register("rooms",views.RoomView,basename="rooms")
router.register("offers",views.OfferView,basename="offers")
router.register("booking",views.BookingView,basename="booking")
router.register("reviews",views.ReviewView,basename="reviews")
urlpatterns=[
   path("token/",ObtainAuthToken.as_view())

]+router.urls