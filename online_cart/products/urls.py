
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.index,name='home'),
    path("product_list", views.list_products,name='list_product'),
    path("product_detail",views.detail_product,name='detail_product'),
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)