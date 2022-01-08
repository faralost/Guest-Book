from django import forms
from django.forms import widgets

from guestbooksapp.models import GuestBookRecord


class RecordForm(forms.ModelForm):
    class Meta:
        model = GuestBookRecord
        fields = ['author', 'email', 'text']
        widgets = {
            'text': widgets.Textarea(attrs={'rows': 5, 'cols': 30})
        }
