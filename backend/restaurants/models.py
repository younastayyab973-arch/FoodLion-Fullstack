from django.db import models


class Category(models.Model):
    """Restaurant category (e.g., Biryani, Cakes, KFC, Dominos)."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Restaurant(models.Model):
    """Restaurant information."""
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    image = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    rating = models.FloatField(default=0, help_text='0-5 star rating')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
