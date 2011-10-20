from django import forms
from humanity.forms import HumanityForm
from nonprofit.mailroom.models import Slot

slot_choices = Slot.objects.filter(enabled=True)

class MailroomForm(HumanityForm):
    slot = forms.ModelChoiceField(queryset=slot_choices, label="I'm looking for information on")
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea)