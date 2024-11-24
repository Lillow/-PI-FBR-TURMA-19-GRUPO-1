from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from api.urls import router

urlpatterns: list = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("auth/", include("rest_framework.urls")),
    path('', include(router.urls))
]
