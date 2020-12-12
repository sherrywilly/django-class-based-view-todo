from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name="home"),
    path('<pk>',views.Tododetail.as_view(),name="detailview"),
    path('update/<pk>',views.Todoupdate.as_view(),name="updateview"),
    path('delete/<pk>',views.Tododelete.as_view(),name="deleteview")
]
