from django.urls import path, include, re_path
from djoser.urls import authtoken
from .views import Do_API, check_token

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path("does/",Do_API.as_view(),name="does"),
    path("does/<int:pk>/",Do_API.as_view(),name="does_pk"),
    path("auth/check_token/", check_token, name="check_token")
]