from django.urls import path
from . import views

urlpatterns = [
    path("", views.addExpense, name="addExpense"),
    path('saveExpense/', views.saveExpense, name='saveExpense')
]