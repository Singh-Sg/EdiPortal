from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def index(request):

    data = InfraVltgDetail.objects.all()
    import pdb; pdb.set_trace()
    context = {'data': data.count()}
    return render(request, 'portal/index.html', context)