from django.shortcuts import render, redirect, get_object_or_404

from guestbooksapp.forms import RecordForm
from guestbooksapp.models import GuestBookRecord


def index(request):
    query = request.GET.get('query')
    records = GuestBookRecord.objects.filter(status='active').order_by('-created_at')
    if query:
        records = GuestBookRecord.objects.filter(author__icontains=query).order_by('-created_at')
        return render(request, 'index.html', {'records': records})
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


def record_update(request, pk):
    record = get_object_or_404(GuestBookRecord, pk=pk)
    if request.method == 'GET':
        form = RecordForm(initial={
            'author': record.author,
            'email': record.email,
            'text': record.text,
        })
        return render(request, 'record_update.html', {'record': record, 'form': form})
    elif request.method == 'POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record.author = form.cleaned_data.get('author')
            record.text = form.cleaned_data.get('text')
            record.email = form.cleaned_data.get('email')
            record.save()
            return redirect('index')
        return render(request, 'record_update.html', {'record': record, 'form': form})


def record_delete(request, pk):
    record = get_object_or_404(GuestBookRecord, pk=pk)
    if request.method == 'GET':
        return render(request, 'record_delete.html', {'record': record})
    elif request.method == 'POST':
        record.delete()
        return redirect('index')
