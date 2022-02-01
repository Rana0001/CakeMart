
from django import forms
from .models import *


class AdminUserForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ("__all__")
