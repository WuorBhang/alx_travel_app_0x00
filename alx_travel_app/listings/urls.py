
from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('listings/', views.ListingListCreateView.as_view(), name='listing-list-create'),
    path('listings/<int:pk>/', views.ListingDetailView.as_view(), name='listing-detail'),
    path('listings/<int:listing_id>/reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('bookings/', views.BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),
    path('search/', views.search_listings, name='search-listings'),
]
