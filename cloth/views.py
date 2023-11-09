from django.shortcuts import get_object_or_404
from . import models, forms
from django.views.generic import ListView, DetailView, CreateView

class ProductView(ListView):
    queryset = models.ProductCL.objects.filter().order_by('-id')
    template_name = 'cloth/product.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter().order_by('-id')

class ProductDetailView(DetailView):
    template_name = 'cloth/product_detail.html'
    success_url = '/products/'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.ProductCL, id=product_id)

class ProductSummerView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='лето')
    template_name = 'cloth/product_summer.html'
    success_url = '/products/'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='лето')

class ProductAutumnView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='осень')
    template_name = 'cloth/product_autumn.html'
    success_url = '/products/'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='осень')

class ProductWinterView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='зима')
    template_name = 'cloth/product_winter.html'
    success_url = '/products/'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='зима')

class ProductSpringView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='весна')
    template_name = 'cloth/product_spring.html'
    success_url = '/products/'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='весна')

class OrderCLView(CreateView):
    template_name = 'cloth/order.html'
    form_class = forms.OrderCLForm
    queryset = models.OrderCL.objects.all()
    success_url = '/products/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(OrderCLView, self).form_valid(form=form)