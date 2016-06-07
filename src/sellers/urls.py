
from django.conf.urls import url, include
from django.contrib import admin
from .views import (
    SellerDashboard,
)

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^create/$', 'products.views.create_view', name="create_view"),
    # url(r'^detail/(?P<object_id>\d+)$', "products.views.detail_view", name="detail_view"),
    # url(r'^detail/(?P<object_id>\d+)/edit/$', "products.views.update_view", name="update_view"),
    # url(r'^detail/(?P<slug>[\w-]+)$', "products.views.detail_slug_view", name="detail_slug_view"),
    # url(r'^list/$', "products.views.list_view", name="list_view"),
    url(r'^$', SellerDashboard.as_view(), name="dashboard"),
]
