from django.shortcuts import render

PRODUCTOS_PRUEBA = [{'nombre': 'Torta Pompadour', 'categoria': 'Tortas', 'descripcion': 'Hojarasca con crema de almendras', 'stock': 4, 'precio': 28000}, {'nombre': 'Kuchen de Nuez', 'categoria': 'Kuchen', 'descripcion': 'Receta alemana', 'stock': 10, 'precio': 16500}, {'nombre': 'Pie de Limon', 'categoria': 'Pies', 'descripcion': 'Merengue suizo dorado', 'stock': 6, 'precio': 14000}, {'nombre': 'Torta de Cuchufli', 'categoria': 'Tortas', 'descripcion': 'Bizcocho relleno rodeado de cuchuflis', 'stock': 5, 'precio': 25000}, {'nombre': 'Torta Panqueque Naranja', 'categoria': 'Tortas', 'descripcion': 'Finas capas con crema de naranja', 'stock': 3, 'precio': 32000}, {'nombre': 'Torta de Milhojas', 'categoria': 'Tortas', 'descripcion': 'Relleno tradicional con manjar', 'stock': 8, 'precio': 26000}]

def home(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        productos = [p for p in PRODUCTOS_PRUEBA if busqueda.lower() in p['nombre'].lower() or busqueda.lower() in p['categoria'].lower()]
    else:
        productos = PRODUCTOS_PRUEBA
    return render(request, 'gestion/index.html', {'productos': productos})