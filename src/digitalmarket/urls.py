"""digitalmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from products.views import ProductListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'create/$', 'products.views.create_view', name="create_view"),
    url(r'^detail/(?P<object_id>\d+)$', "products.views.detail_view", name="detail_view"),
    url(r'^detail/(?P<object_id>\d+)/edit/$', "products.views.update_view", name="update_view"),
    url(r'^detail/(?P<slug>[\w-]+)$', "products.views.detail_slug_view", name="detail_slug_view"),
    url(r'^list/$', "products.views.list_view", name="list_view"),
    url(r'^products/list/$', ProductListView.as_view(), name="product_list_view")
]
