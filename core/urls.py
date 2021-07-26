from core.views.transbankpay import webpay_plus_create
from django.urls import path
# Importaciones para views
from core.views.cart import cart
from core.views.home import home
from core.views.transbankpay import commitpay, webpay_plus_create

# Importar metodo para acceder a archivos estaticos
from django.conf.urls.static import static
# Importar settings
from django.conf import settings
urlpatterns = [
    path('',home,name="home"),
    path('cart/',cart, name='cart'),
    path('commit-pay/', commitpay),
    path('webpay-plus-create/', webpay_plus_create),  
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
