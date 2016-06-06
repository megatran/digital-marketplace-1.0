from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductAddForm, ProductModelForm
# Create your views here.

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
    template = "create_view.html"
    context = {
        "form": form,
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
    template = "detail_view.html"
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
    template = "update_view.html"
    context={
        "object": product,
        "form": form,
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


