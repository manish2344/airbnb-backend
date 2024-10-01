from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Listing
        fields = ['id', 'user', 'title', 'description', 'price_per_night', 'location', 'image','image_url', 'amenities', 'category', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
    # def validate_image(self, value):
    #     if value.size > 1024 * 1024 * 2:  # 2 MB
    #         raise serializers.ValidationError("The image file size must be under 2MB.")
    #     return value


    def get_image_url(self, obj):
        return obj.image.url


# from rest_framework import serializers
# from .models import Listing

# class ListingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Listing
#         fields = ['id', 'user', 'title', 'description', 'price_per_night', 'location', 'image', 'amenities', 'category', 'created_at', 'updated_at']
#         read_only_fields = ['id', 'user', 'created_at', 'updated_at']



# listings/serializers.py

# from rest_framework import serializers
# from .models import Listing, Category, Amenity

# class AmenitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Amenity
#         fields = ['id', 'name']
#         read_only_fields = ['id']

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name']
#         read_only_fields = ['id']

# class ListingSerializer(serializers.ModelSerializer):
#     amenities = AmenitySerializer(many=True, read_only=True)
#     category = CategorySerializer(read_only=True)
#     category_id = serializers.PrimaryKeyRelatedField(
#         queryset=Category.objects.all(),
#         source='category',
#         write_only=True
#     )
#     amenities_ids = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Amenity.objects.all(),
#         source='amenities',
#         write_only=True
#     )
#     user = serializers.StringRelatedField(read_only=True)
#     slug = serializers.SlugField(read_only=True)
#     image = serializers.ImageField(required=False, allow_null=True)

#     class Meta:
#         model = Listing
#         fields = [
#             'id',
#             'user',
#             'title',
#             'slug',
#             'description',
#             'price_per_night',
#             'city',
#             'state',
#             'country',
#             'latitude',
#             'longitude',
#             'image',
#             'category',
#             'category_id',
#             'amenities',
#             'amenities_ids',
#             'is_active',
#             'created_at',
#             'updated_at'
#         ]
#         read_only_fields = [
#             'id',
#             'user',
#             'slug',
#             'amenities',
#             'category',
#             'is_active',
#             'created_at',
#             'updated_at'
#         ]

#     def validate_image(self, value):
#         if value:
#             if value.size > 5 * 1024 * 1024:  # 5MB limit
#                 raise serializers.ValidationError("Image size should not exceed 5MB.")
#             if not value.content_type.startswith('image/'):
#                 raise serializers.ValidationError("Invalid image type.")
#         return value

#     def create(self, validated_data):
#         amenities = validated_data.pop('amenities', [])
#         category = validated_data.pop('category', None)
#         listing = Listing.objects.create(category=category, **validated_data)
#         listing.amenities.set(amenities)
#         return listing

#     def update(self, instance, validated_data):
#         amenities = validated_data.pop('amenities', None)
#         category = validated_data.pop('category', None)
        
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
        
#         if category is not None:
#             instance.category = category

#         if amenities is not None:
#             instance.amenities.set(amenities)
        
#         instance.save()
#         return instance
