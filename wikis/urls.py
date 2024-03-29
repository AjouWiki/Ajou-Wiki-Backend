from django.urls import path
from . import views

urlpatterns = [
    path("", views.Wikis.as_view()),
    path("<int:pk>", views.WikiDetail.as_view()),
    path("<int:pk>/<int:detail_pk>", views.WikiDetailAPi.as_view()),
    path("search/<str:keyword>", views.SearchWiki.as_view()),
    # path("<int:pk>/reviews", views.RoomReviews.as_view()),
    # path("<int:pk>/photos", views.RoomPhotos.as_view()),
    # path("amenities/", views.Amenities.as_view()),
    # path("<int:pk>/bookings", views.RoomBookings.as_view()),
    # path("amenities/<int:pk>", views.AmenityDetail.as_view()),
]
