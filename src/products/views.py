from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def detail_view(request, object_id=None):
    #1 item
    product = get_object_or_404(Product, id=object_id)
    template = "detail_view.html"
    context={
        "object": product
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


