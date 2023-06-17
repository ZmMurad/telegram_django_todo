
from django.urls import path
from .views import DoList, Do_Detail, do_delete
urlpatterns = [
    path("",DoList.as_view(),name="home"),
    path("<int:id>/", Do_Detail.as_view(),name="do_detail"),
    path("delete/<int:id>/", do_delete,name="delete")
]
