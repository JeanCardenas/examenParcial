from django.shortcuts import render

def productos(request):
    return render(request, 'productos.html')

def tiendas(request):
    return render(request, 'tiendas.html')

def detalle_tienda(request, tienda_id):

    return render(request, 'detalle_tienda.html', {'tienda_id': tienda_id})