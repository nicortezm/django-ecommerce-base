from django.shortcuts import render
from core.models import Producto
def cart(request):
    print('cart')

    productos = Producto.objects.all()
    total = 0
    for prod in productos:
        total += prod.precio
    # control = { 'image' : 'core/img/product/control-xbox.jpg',
    #             'product': 'XBOX GAMEPAD',
    #             'description': 'BLACK COLOR',
    #             'price' : 59000,
    #             'quantity': 1
    #             }
    # gabinete = {'image' : 'core/img/product/gabinete.jpg',
    #             'product': 'CABINET',
    #             'description': 'BLACK MATE COLOR',    
    #             'price' : 69000,
    #             'quantity': 1
    #             }
    # notebook = {'image' : 'core/img/product/notebook.jpg',
    #             'product': 'GAMER LAPTOP',
    #             'description': 'WHITE COLOR',    
    #             'price' : 2150000,
    #             'quantity': 1
    #             }                   

    # products = [control, gabinete, notebook]
    # total = control.get('price') + gabinete.get('price') + notebook.get('price')

    return render(request, 'core/cart.html', {'products' : productos, 'total': total})
    # return render(request, 'core/cart.html')
    