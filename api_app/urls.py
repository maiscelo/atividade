from django.urls import path
from .views import MonicaoViews
from .views import ArmaViews

urlpatterns = [
    path('monicao/', MonicaoViews.as_view()),
    path('arma/', ArmaViews.as_view())
]
