from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views import View
from myflex.tasks import prueba_suma
import time


class RegisterView(View):
    def get(self, request):
        return render(request, 'flexer/register.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'flexer/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'flexer/profile.html')


class TestPage(View):
    def get(self, request):
        resultado = prueba_suma.delay(5, 6)
        return HttpResponse("work kicked off!")