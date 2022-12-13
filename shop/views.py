
from django.shortcuts import get_object_or_404, render
from .models import Category,Product
from django.views.generic import ListView, DetailView

# Create your views here.


# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'shop/product/list.html',
#             {'category': category,
#             'categories': categories,
#             'products': products})
    
class CategoryByProductView(ListView):
    model = Product
    context_object_name = 'products'
    template_name='shop/product/list.html'
      
    def get_queryset(self):
        if 'category_slug' in self.kwargs:
            return Product.objects.filter(category__slug=self.kwargs['category_slug'])
        return Product.objects.filter(available=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        categories = Category.objects.all()         
        if 'category_slug' in self.kwargs:
             category = Category.objects.get(slug=self.kwargs["category_slug"])
             context['title'] =  str(context['products'][0].category)
        else:
             category = None
        context["categories"] = categories
        context["category"] = category
        return context
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product/detail.html'
    pk_url_kwarg = "id"
    slug_url_kwarg = 'slug'