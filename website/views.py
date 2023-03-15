from django.shortcuts import render
from .models import Workers
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    workers = Workers.objects.all()
    context = {
        'workers': workers
    }
    return render(request, 'website/index.html', context)


def Worker(request, id):
    worker = Workers.objects.filter(pk=id)
    contex = {
        "data": worker
    }
    return render(request, 'website/worker.html', contex)

@login_required()
def Search(request):
    workers = Workers.objects.order_by('-date_creat')
    if 'workerName' in request.GET:
        name = request.GET['workerName']
        if name:
            workers = Workers.objects.filter(Q(name__iexact=name) | Q(last_name__iexact=name))
    context = {
        'workers': workers
    }
    return render(request, 'website/search.html', context)



