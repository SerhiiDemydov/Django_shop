from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ProductUpdateForm
from .models import Product, PublishingHouse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views import generic

# Create your views here.


def home_page(request):
    products = Product.objects.all()
    return render(request,'home_page.html', context={"products": products})


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'language', 'time', 'max_players', 'min_players', 'min_age_player', 'type']
    template_name = 'product_create_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.slug = obj.name.replace(' ','-')
        obj.publishing_house = self.get_publishinghouse()
        obj.save()
        return redirect(obj.get_absolute_url())

    def get_publishinghouse(self):
        return get_object_or_404(PublishingHouse, owner=self.request.user)


class BookListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'  # ваше собственное имя переменной контекста в шаблоне
    queryset = Product.objects.all()
    template_name = 'home_page.html'
    paginate_by = 6



class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'product_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if request.user.is_authenticated and product.publishing_house.owner.id == request.user.id:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/')

