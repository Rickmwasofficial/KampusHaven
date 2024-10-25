from django.db import models
from datetime import datetime
from django.urls import reverse
import base64
from urllib.parse import quote

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=100000)
    posted_on = models.DateTimeField(auto_now_add=True)
    finder_no = models.CharField(max_length=10)
    finder_email = models.EmailField()
    state = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='products/') 

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            # First save to get an Id
            super().save(*args, **kwargs)
            # The create slug with Id and save again
            self.slug = slugify(f"{self.name}-{self.id}")
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def get_image_base64(self):
        """Convert ImageField to base64 string"""
        if self.image:
            try:
                with self.image.open('rb') as img_file:
                    return base64.b64encode(img_file.read()).decode('utf-8')
            except Exception:
                return None
        return None

    def get_share_links(self):
        """Generate sharing links for different platforms"""
        product_url = f"https://kampushaven.onrender.com{self.get_absolute_url()}"
        return {
            'whatsapp': f"https://api.whatsapp.com/send?text={self.name} - {product_url}",
            'facebook': f"https://www.facebook.com/sharer/sharer.php?u={product_url}",
            'twitter': f"https://twitter.com/intent/tweet?text={self.name}&url={product_url}"
        }
