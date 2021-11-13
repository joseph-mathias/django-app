from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product

def home(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'products/home.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'

    ordering = ['-date_posted']


class ProductDetailView(DetailView):
    model = Product



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'discription','old_price', 'new_price', 'stock', 'product_img']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'discription','old_price', 'new_price', 'stock', 'product_img']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False


class SearchResultsView(ListView):
    model = Product
    template_name = 'products/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(title__icontains=query) | Q(new_price__icontains=query)
        )
        return object_list

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
            product = self.get_object()
            if self.request.user == product.author:
                return True
            return False


def about(request):
    return render(request,'products/test.html')

