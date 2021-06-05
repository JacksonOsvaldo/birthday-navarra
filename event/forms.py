from django import forms
from .models import UserEvent

# Formulário que herda os campos do model UserEvent
class UserForm(forms.ModelForm):
    class Meta:
        model = UserEvent
        fields = "__all__"
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }
