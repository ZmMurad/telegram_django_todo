from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Does

class DoForm(forms.ModelForm):
    class Meta:
        model=Does
        fields=["title","text","active"]
        widgets={"title":forms.TextInput(attrs={"class":"form-control"}),"text":forms.TextInput(attrs={"class":"form-control"}),"active":forms.CheckboxInput(attrs={"class":"form-check-input"})}
        labels={"title":"Заголовок", "text":"Ваша запись"}
 