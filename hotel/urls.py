from django.urls import path
from hotel import views
urlpatterns=[

    path("", views.HomeView.as_view(),name='base'),
    path("register",views.SignUpView.as_view(),name="signup"),
    path("login",views.SigninView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="index"),
    path("owner/register",views.HotelOwnerRegistrationView.as_view(),name="o-signup"),
    path("owner/signin",views.HotelOwnerLoginView.as_view(),name="o-signin"),
    path("owner/index",views.OIndex.as_view(),name="o-index"),
    path("u-profile/add",views.UserProfileCreateView.as_view(),name="user-profile-add"),
    path("u-profile/details",views.ProfileDetailView.as_view(),name="user-profile-detail"),
    path("u-profile/<int:id>/change",views.ProfileUpdateView.as_view(),name="user-profile-edit"),
    path("o-profiles/add",views.OwnerProfileCreateView.as_view(),name="owner-profile-add"),
    path("o-profiles/details",views.OwnerProfileDetailView.as_view(),name="owner-profile-detail"),
    path("o-profiles/<int:id>/change",views.OwnerProfileUpdateView.as_view(),name="owner-profile-edit"),
    path("place/add",views.PlaceCreateView.as_view(),name="place-add"),
    path("place/list",views.PlaceListView.as_view(),name="place-list"),
    path("hotel/add",views.HotelCreateView.as_view(),name="hotel-add"),
    path("hotel/list",views.HotelListView.as_view(),name="hotel-list"),
    path("hotel/<int:id>/detail",views.HotelDetailView.as_view(),name="hotel-detail"),
    path("hotel/<int:id>/remove",views.HotelDeleteView.as_view(),name="hotel-delete"),
    path("hotel/<int:id>/change",views.HotelEditView.as_view(),name="hotel-edit"),
    path("room/add",views.RoomCreateView.as_view(),name="room-add"),
    path("room/list",views.RoomListView.as_view(),name="room-list"),
    path("room/<int:id>/detail",views.RoomDetailView.as_view(),name="room-detail"),
    path("room/<int:id>/change",views.RoomEditView.as_view(),name="room-edit"),
    path("room/<int:id>/remove",views.RoomDeleteView.as_view(),name="room-delete"),
    path("booking/<int:id>",views.BookingView.as_view(),name="create-booking"),
    path("booking/<int:id>/list",views.BookingListView.as_view(),name="booking-list"),
    path("booking/<int:id>/cancel",views.BookingCancelView.as_view(),name="booking-cancel"),
    path("offers/add",views.OfferCreateView.as_view(),name="offer-add"),
    path("offers/all",views.OffersView.as_view(),name="offer-list"),
    path("reviews/<int:id>/add",views.ReviewCreateView.as_view(),name="review-add"),
    path("logout",views.SignoutView.as_view(),name="signout")

]