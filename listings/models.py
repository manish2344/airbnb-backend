# from django.db import models
# from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField  # Import CloudinaryField


# class Listing(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
#     location = models.CharField(max_length=255)
#     # image = models.ImageField(upload_to='listings/images/', blank=True, null=True)  # Optional image
#     image = models.ImageField(upload_to='profile_pics/')
#     # image = CloudinaryField('image') 
#     # image = CloudinaryField('image', default='default_avatar.jpg')
#     amenities = models.JSONField(default=list)  # Store amenities as a JSON list
#     category = models.CharField(max_length=100)  # Simple category field
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title



# from django.db import models
# from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField  # Import CloudinaryField

# class Listing(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
#     location = models.CharField(max_length=255)
#     image = CloudinaryField('image')  # Use CloudinaryField for image storage
#     amenities = models.JSONField(default=list)  # Store amenities as a JSON list
#     category = models.CharField(max_length=100)  # Simple category field
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title



# listings/models.py

# from django.db import models
# from django.conf import settings
# from cloudinary.models import CloudinaryField  # Import CloudinaryField
# from django.utils.text import slugify
# from django.core.validators import MinValueValidator
# from django.core.exceptions import ValidationError

# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     class Meta:
#         verbose_name_plural = 'Categories'
#         ordering = ['name']

#     def __str__(self):
#         return self.name

# class Amenity(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     class Meta:
#         ordering = ['name']

#     def __str__(self):
#         return self.name

# class Listing(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='listings'
#     )
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True, blank=True)
#     description = models.TextField()
#     price_per_night = models.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         validators=[MinValueValidator(0)]
#     )
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100, blank=True, null=True)
#     country = models.CharField(max_length=100)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     image = CloudinaryField('image', blank=True, null=True, default='default_listing_image.jpg')
#     amenities = models.ManyToManyField(Amenity, related_name='listings', blank=True)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='listings')
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     objects = models.Manager()  # Default manager
#     active = models.Manager()    # Custom manager can be implemented as needed

#     class Meta:
#         ordering = ['-created_at']
#         unique_together = ('user', 'title')

#     def __str__(self):
#         return f"{self.title} by {self.user.username}"

#     def clean(self):
#         if self.price_per_night < 0:
#             raise ValidationError('Price per night cannot be negative.')

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             base_slug = slugify(self.title)
#             slug = base_slug
#             counter = 1
#             while Listing.objects.filter(slug=slug).exists():
#                 slug = f"{base_slug}-{counter}"
#                 counter += 1
#             self.slug = slug
#         self.full_clean()
#         super().save(*args, **kwargs)



from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    image = CloudinaryField('image')
    amenities = models.JSONField(default=list)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title