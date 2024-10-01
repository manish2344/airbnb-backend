from django.urls import path
from .views import ListingListCreateView, ListingDetailView

urlpatterns = [
    path('', ListingListCreateView.as_view(), name='listing-list-create'),  # GET and POST
    path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),   # GET, PUT, DELETE
]
