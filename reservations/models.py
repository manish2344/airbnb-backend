# # reservations/models.py
# from django.db import models
# from django.contrib.auth.models import User

# class Reservation(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
#     listing = models.ForeignKey('listings.Listing', on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Reservation by {self.user.username} for {self.listing.title}'
# from django.db import models
# from django.contrib.auth.models import User


# # class Listing(models.Model):
# #     # ... (existing Listing model)
# class Reservation(models.Model):
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reservations')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
#     start_date = models.DateField()
#     end_date = models.DateField()
#     guests = models.IntegerField()
#     status = models.CharField(max_length=20, choices=[
#         ('pending', 'Pending'),
#         ('accepted', 'Accepted'),
#         ('declined', 'Declined'),
#         ('cancelled', 'Cancelled')
#     ])
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.listing.title} - {self.start_date} to {self.end_date}"



# from django.db import models
# from django.contrib.auth.models import User
# from listings.models import Listing  # Add this import

# class Reservation(models.Model):
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reservations')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
#     start_date = models.DateField()
#     end_date = models.DateField()
#     # guest_count = models.IntegerField()
#     # total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Reservation for {self.listing.title} by {self.user.username}"



# reservations/models.py
from django.db import models
from django.contrib.auth.models import User
from listings.models import Listing  # Add this import

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Reservation by {self.user.username} for {self.listing.title}'
