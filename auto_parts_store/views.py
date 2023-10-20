from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms

def avtopartsListView(request):
    avtoparts = models.AutoParts.objects.all()
    html_name = 'avto_parts/avtoparts_list.html'
    context = {
        'avtoparts_key': avtoparts,
    }
    return render(request, html_name, context)

def avtopartsDetailView(request, id):
    avtoparts_id = get_object_or_404(models.AutoParts, id=id)
    html_name = 'avto_parts/avtoparts_detail.html'
    context = {
        'avtoparts_id': avtoparts_id,
    }
    return render(request, html_name, context)

def createProductsView(request):
    method = request.method
    if method == "POST":
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Товар успешно добавлен')
    else:
        form = forms.ProductForm()

    return render(request, 'avto_parts/create_product.html', {'form': form})

def deleteProductsView(request, id):
    product_id = get_object_or_404(models.AutoParts, id=id)
    product_id.delete()
    return HttpResponse('Товар успешно удалён')

def updateProductsView(request, id):
    product_id = get_object_or_404(models.AutoParts, id=id)
    if request.method == 'POST':
        form = forms.ProductForm(instance=product_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Товар изменён')

    else:
        form = forms.ProductForm(instance=product_id)
    return render(request, 'avto_parts/update_product.html',
                  {
                      'form': form,
                      'product_id': product_id
                  }
                  )