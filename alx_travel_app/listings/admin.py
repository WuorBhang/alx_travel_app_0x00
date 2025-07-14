
from django.contrib import admin
from .models import Listing, Review, Booking

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'listing_type', 'price_per_night', 'host', 'is_active', 'created_at']
    list_filter = ['listing_type', 'is_active', 'created_at', 'location']
    search_fields = ['title', 'description', 'location']
    list_editable = ['is_active']
    date_hierarchy = 'created_at'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['listing', 'reviewer', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['listing__title', 'reviewer__username', 'comment']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['listing', 'guest', 'check_in', 'check_out', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'created_at', 'check_in']
    search_fields = ['listing__title', 'guest__username']
    list_editable = ['status']
    date_hierarchy = 'created_at'
