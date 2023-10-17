from django.shortcuts import render, get_object_or_404
from . import models

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