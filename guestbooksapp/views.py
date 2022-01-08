from django.shortcuts import render, redirect

from guestbooksapp.forms import RecordForm
from guestbooksapp.models import GuestBookRecord


def index(request):
    records = GuestBookRecord.objects.all()
    return render(request, 'index.html', {'records': records})


def record_add(request):
    if request.method == 'GET':
        form = RecordForm()
        return render(request, 'record_add.html', {'form': form})
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'record_add.html', {'form': form})
