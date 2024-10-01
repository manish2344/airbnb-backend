
# reservations/serializers.py
from rest_framework import serializers
from .models import Reservation
from listings.models import Listing
from listings.serializers import ListingSerializer  # Add this import

class ReservationSerializer(serializers.ModelSerializer):
    listing_id = serializers.PrimaryKeyRelatedField(
        queryset=Listing.objects.all(),
        source='listing',
        write_only=True
    )
    listing = ListingSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id',
            'listing',
            'listing_id',
            'start_date',
            'end_date',
            'created_at',
            'user'
        ]
        read_only_fields = ['id', 'created_at', 'user']
