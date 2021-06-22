class relleno():
    def form_mod_producto(request,id):
        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, instance = producto)
            if producto.is_valid:
                producto.save()
                return redirect('preventa')
        return render(request, 'valhalla/templates/#', datos)

    def form_del_producto(request,id):
            producto = Producto.objects.get(ñ = id) #la Ñ es por rellenar, lo mismo con el #
            producto.delete()
            return redirect('preventa')