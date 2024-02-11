

from django.urls import path, re_path, register_converter
from . import views
from. import converters

register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about),
    path('kub/', views.kub, name='kub'),
    path('animals/', views.animals),
    path('cat/<slug:cat_slug>/', views.category_slug),
    path('cat/<slug:post_slug>/', views.show_post, name='post'),
    path("archive/<year4:year>/", views.archive, name='archive')


]
