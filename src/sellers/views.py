from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormMixin
from .forms import NewSellerForm

# Create your views here.

from digitalmarket.mixins import LoginRequiredMixin

class SellerDashboard(LoginRequiredMixin,View):
    form_class = NewSellerForm
    success_url = "/seller/"
    def post(self, request, *args, **kwargs):
        form = NewSellerForm(request.POST)
        if form.is_valid():
            print "make the user apply model"
        return render(request, "sellers/dashboard.html", {"form":form})

    def get(self, request, *args, **kwargs):
        form = NewSellerForm(request.POST or None)
        return render(request, "sellers/dashboard.html", {"form":form})
    def form_valid(self, form):
        valid_data = super(SellerDashboard, self).form_valid(form)
        return valid_data