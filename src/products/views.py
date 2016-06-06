from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Product
from .forms import ProductAddForm, ProductModelForm
# Create your views here.

class ProductListView(ListView):
    model= Product
    # template_name = "list_view.html"
    #
    # def get_context_data(self, **kwargs):
    #     context= super(ProductListView, self).get_context_data(**kwargs)
    #     print context
    #     context["queryset"] = self.get_queryset()
    #     return context
    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(**kwargs)
        #qs = qs.filter(title__icontains="Product")
        return qs

def create_view(request):
    #ProductAddFORM
    # form = ProductAddForm(request.POST or None)
    # if form.is_valid():
    #     data = form.cleaned_data
    #     title = data.get("title")
    #     description = data.get("description")
    #     price = data.get("price")
    #     #new_obj = Product.objects.create(title=title, description=description, price=price)
    #     new_obj = Product()
    #     new_obj.title = title
    #     new_obj.description = description
    #     new_obj.price = price
    #     new_obj.save()

    #PRODUCT MODEL FORM method:
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.sale_price = instance.price
        instance.save()
    template = "form.html"
    context = {
        "form": form,
        "submit_btn": "Create Product"
    }
    return render(request, template, context)


def detail_slug_view(request, slug=None):
    try:
        product = get_object_or_404(Product, slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by("-title").first()
    print slug
    template = "detail_view.html"
    context={
        "object": product
    }
    return render(request, template, context)

def detail_view(request, object_id=None):
    #1 item
    product = get_object_or_404(Product, id=object_id)
    template = ""
    context={
        "object": product
    }
    return render(request, template, context)

def update_view(request, object_id=None):
    #1 item
    product = get_object_or_404(Product, id=object_id)
    form = ProductModelForm(request.POST or None, instance=product)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    template = "form.html"
    context={
        "object": product,
        "form": form,
        "submit_btn": "Update Product"
    }
    return render(request, template, context)


def list_view(request):
    #list of items
    print request
    queryset = Product.objects.all()
    template = "list_view.html"
    context={
        "queryset": queryset
    }
    return render(request, template, context)

# def detail_view(request):
#     print request
#     template = "detail_view.html"
#     context={}
#     return render(request, template, context)
#
# def detail_view(request):
#     print request
#     template = "detail_view.html"
#     context={}
#     return render(request, template, context)
#


