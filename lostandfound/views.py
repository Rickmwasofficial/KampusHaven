from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product
from django.http import HttpResponse
import os
from .forms import ProductForm
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
    

class create_product(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.posted_on = timezone.now()
        messages.success(self.request, 'Product was created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error creating the product.')
        return super().form_invalid(form)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    # Generate actual image file of OG tags
    if not os.path.exists('media/products/'):
        os.makedirs('media/products/')

    img_path = f'media/products/{product.slug}.jpg'
    if not os.path.exists(img_path):
        with open(img_path, 'wb') as f:
            f.write(product.image)

    context = {
        'product': product,
        'share_links': product.get_share_links(),
        'og_image_url': f'https://kampushaven.onrender.com/media/products/{product.slug}.jpg'
    }
    return render(request, 'details.html', context)
