from django.shortcuts import render
from .models import Trix
from .forms import TrixForm
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def index(request):
    return render(request,'index.html')

def trix_list(request):
    trixs = Trix.objects.all().order_by('-created_at')
    return render(request,'trix_list.html', {'trixs': trixs})

def trix_create(request):
    if request.method == 'POST':
        form = TrixForm(request.POST, request.FILES)
        if form.is_valid():
            trix = form.save(commit=False)
            trix.user = request.user
            trix.save()
            return redirect('trix_list')

    else:
        form = TrixForm()
    return render(request, 'trix_form.html',{'form':form})

def trix_edit(request,trix_id):
    trix = get_object_or_404(Trix, pk=trix_id,user = request.user)
    if request.method == 'POST':
        form = TrixForm(request.POST, request.FILES,instance=trix)
        if form.is_valid():
            trix = form.save(commit=False)
            trix.user = request.user
            trix.save()
            return redirect('trix_list')
    else:
        form = TrixForm(instance=trix)
    return render(request, 'trix_form.html',{'form':form})

def trix_delete(request, trix_id):
    trix = get_object_or_404(Trix,pk=trix_id,user = request.user)
    if request.method == 'POST':
        trix.delete()
        return redirect('trix_list')
    return render(request, 'trix_del_conf.html',{'trix':trix})