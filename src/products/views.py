import os

from mimetypes import guess_type
from django.db.models import Q
from django.conf import settings
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.core.servers.basehttp import FileWrapper
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .mixins import ProductManagerMixin

from digitalmarket.mixins import (
    MultiSlugMixin,
    SubmitBtnMixin,
    LoginRequiredMixin
)
from .models import Product
from .forms import ProductAddForm, ProductModelForm
# Create your views here.


class ProductCreateView(LoginRequiredMixin,SubmitBtnMixin,CreateView):
    model = Product
    template_name = "form.html"
    form_class = ProductModelForm
    #success_url = "/products/add/"
    submit_btn = "Add Product"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        #finish off saving database
        valid_data = super(ProductCreateView, self).form_valid(form)
        form.instance.managers.add(user)
        # add all default users
        return valid_data
    # def get_success_url(self):
    #     return reverse("products:list")

class ProductUpdateView(ProductManagerMixin, SubmitBtnMixin, MultiSlugMixin, UpdateView):
    model = Product
    template_name = "form.html"
    form_class = ProductModelForm
    success_url = "/products/"
    submit_btn = "Update Product"

    #already in ProductManagerMixin
    # def get_object(self, *args, **kwargs):
    #     user = self.request.user
    #     obj = super(ProductUpdateView, self).get_object(*args, **kwargs)
    #     if obj.user == user or user in obj.managers.all():
    #         return obj
    #     else:
    #         raise Http404

class ProductDownloadView(MultiSlugMixin, DetailView):
    model = Product

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj in request.user.myproducts.products.all():
            filepath = os.path.join(settings.PROTECTED_ROOT, obj.media.path)
            guessed_type = guess_type(filepath)[0]
            wrapper = FileWrapper(file(filepath))
            mimetype = "application/force-download"
            if guessed_type:
                mimetype = guessed_type
            response = HttpResponse(wrapper, content_type=mimetype)

            if not request.GET.get("preview"):
                response["Content-Disposition"] = "attachment; filename=%s" % (obj.media.name)
            response["X-SendFile"] = str(obj.media.name)
            return response
        else:
            raise Http404

class ProductDetailView(MultiSlugMixin, DetailView):
    model = Product

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
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            ).order_by("title")
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


