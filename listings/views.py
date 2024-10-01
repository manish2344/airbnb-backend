# from rest_framework import generics, permissions
# from .models import Listing
# from .serializers import ListingSerializer

# class ListingListCreateView(generics.ListCreateAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)  # Associate listing with the logged-in user

# class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]






import logging
from rest_framework import generics, permissions
from .models import Listing
from .serializers import ListingSerializer

logger = logging.getLogger(__name__)

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        logger.debug(f"Attempting to create new listing. User: {self.request.user}, Data: {serializer.validated_data}")
        try:
            instance = serializer.save(user=self.request.user)
            logger.info(f"Listing created successfully. ID: {instance.id}")
        except Exception as e:
            logger.error(f"Error creating listing: {str(e)}", exc_info=True)
            raise

class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        logger.debug(f"Attempting to update listing. User: {self.request.user}, Data: {serializer.validated_data}")
        try:
            instance = serializer.save()
            logger.info(f"Listing updated successfully. ID: {instance.id}")
        except Exception as e:
            logger.error(f"Error updating listing: {str(e)}", exc_info=True)
            raise

    def perform_destroy(self, instance):
        logger.debug(f"Attempting to delete listing. User: {self.request.user}, Listing ID: {instance.id}")
        try:
            instance.delete()
            logger.info(f"Listing deleted successfully. ID: {instance.id}")
        except Exception as e:
            logger.error(f"Error deleting listing: {str(e)}", exc_info=True)
            raise





# listings/views.py

# from rest_framework import generics, permissions, filters
# from django_filters.rest_framework import DjangoFilterBackend
# from django.db.models import Q
# from .models import Listing
# from .serializers import ListingSerializer
# from .permissions import IsOwnerOrReadOnly
# from rest_framework.pagination import PageNumberPagination

# class ListingPagination(PageNumberPagination):
#     page_size = 10  # Adjust as needed
#     page_size_query_param = 'page_size'
#     max_page_size = 100

# class ListingListCreateView(generics.ListCreateAPIView):
#     serializer_class = ListingSerializer
#     pagination_class = ListingPagination
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['category__name', 'city', 'price_per_night']
#     search_fields = ['title', 'description', 'city', 'state', 'country']
#     ordering_fields = ['price_per_night', 'created_at']
#     ordering = ['-created_at']

#     def get_permissions(self):
#         if self.request.method == 'POST':
#             return [permissions.IsAuthenticated()]
#         return [permissions.AllowAny()]

#     def get_queryset(self):
#         user = self.request.user
#         queryset = Listing.objects.filter(is_active=True)
#         if user.is_authenticated:
#             queryset = Listing.objects.filter(Q(is_active=True) | Q(user=user))
#         return queryset.select_related('user', 'category').prefetch_related('amenities')

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_queryset(self):
#         user = self.request.user
#         queryset = Listing.objects.filter(is_active=True)
#         if user.is_authenticated:
#             queryset = Listing.objects.filter(Q(is_active=True) | Q(user=user))
#         return queryset.select_related('user', 'category').prefetch_related('amenities')

#     def delete(self, request, *args, **kwargs):
#         """
#         Override delete to implement soft deletion.
#         """
#         listing = self.get_object()
#         listing.is_active = False
#         listing.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
