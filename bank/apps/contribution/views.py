from django.shortcuts import render
from django.views.generic.base import View

from .models import *


class BankView(View):
    def get(self, request):
        contribution = Bank.objects.all()
        return render(request, 'contribution/home.html', {'home': contribution})


def checkout(request):
    bank = Bank.objects.all()
    return render(request, 'bank/checkout.html', {'checkout': bank})


def last(request):
    exit = Bank.objects.all()
    return render(request, 'exit/last.html', {'last': exit})

