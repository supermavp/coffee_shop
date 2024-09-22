from django.views import generic

from products.forms import ProductForm

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm