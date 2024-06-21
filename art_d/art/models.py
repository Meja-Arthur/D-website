from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class ArtCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name
    
class Painter(models.Model):
    name = models.CharField(max_length=225)
    about  = models.TextField(blank=True)
    image = models.ImageField(upload_to='painter_image/', blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
    
    
class Art(models.Model):  
    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True, default='')
    category = models.ForeignKey(ArtCategory, on_delete=models.CASCADE, related_name='product')
    owner = models.ForeignKey(Painter, on_delete=models.CASCADE, related_name='art')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    in_stock = models.BooleanField(default=False)
    out_stock = models.BooleanField(default=False)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.name
    
    @classmethod
    def filter_by_price_range(cls, min_price, max_price):
         """
         Custom method to filter books by price range.
         """
         return cls.objects.filter(price__gte=min_price, price__lte=max_price)

    def save(self, *args, **kwargs):
         """
         Override the save method to automatically generate a slug based on the title.
         """
         if not self.slug:
             self.slug = slugify(self.title)
         super().save(*args, **kwargs)

    @classmethod
    def get_in_stock(cls):
         """
         Custom method to get all "must read" books.
         """
         return cls.objects.filter(in_stock=True)

    @classmethod
    def get_out_of_stock(cls):
         """
         Custom method to get all "recommended" books.
         """
         return cls.objects.filter( out_stock=True)
  
class ArtImage(models.Model):
    art = models.ForeignKey(Art, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='art_images/')
    
    def _str__(self):
        return f"image for {self.art.name }"