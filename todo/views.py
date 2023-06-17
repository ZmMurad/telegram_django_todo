from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Does
from django.views.generic import ListView, DetailView, DeleteView
# Create your views here.
from django.contrib.auth import get_user
from .forms import DoForm
from django.contrib.auth.mixins import LoginRequiredMixin


class DoList(ListView ):
    model=Does
    context_object_name="does_list"
    template_name="index.html"
    paginate_by = 25
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data=super().get_context_data(**kwargs)
        does_by_owner=Does.objects.filter(user=get_user(self.request))
        data["does_list"]=does_by_owner
        data["form"]=DoForm()
        return data
    def post(self,request,*args, **kwargs):
        form=DoForm(self.request.POST)
        if form.is_valid():
            form=form.cleaned_data
            Does.objects.create(title=form.get("title"),text=form.get("text"),user=get_user(request))
            return redirect("home")
        return super().get(request,*args, **kwargs)
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if str(request.user)=="AnonymousUser":
            text="Вы должны авторизоваться"            
            return render(request, "index.html",{"text":text})
        return super().get(request, *args, **kwargs) 

class Do_Detail(DetailView):
    template_name="detail_do.html"
    context_object_name="do"
    model=Does
    pk_url_kwarg = 'id'
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data=super().get_context_data(**kwargs)
        data["form"]=DoForm(initial={"active":self.get_object().active})
        return data 
    def post(self,request,*args, **kwargs):
        form=DoForm(self.request.POST)
        if form.is_valid():
            form=form.cleaned_data
            self.object=self.get_object()
            Does.objects.filter(id=self.object.id).update(title=form.get("title"),text=form.get("text"),active=form.get("active"))
            return redirect("do_detail",self.object.id)
        return super().get(request,*args, **kwargs)
    
def do_delete(request,id):
    Does.objects.filter(id=id).delete()
    return redirect("home")
