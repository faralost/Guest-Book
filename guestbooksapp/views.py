from django.shortcuts import render

from guestbooksapp.models import GuestBookRecord


def index(request):
    records = GuestBookRecord.objects.all()
    return render(request, 'index.html', {'records': records})
