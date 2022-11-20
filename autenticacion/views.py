from django.shortcuts import render, redirect
from django.views.generic import View
from gestionTurnos.forms import AdminFormCrearUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

class URegistro(View):

    def get(self, request):
        form = AdminFormCrearUser()
        return render(request, "registro.html", {"form": form})

    def post(self, request):
        form =AdminFormCrearUser(request.POST, request.FILES)
        if form.is_valid():
            
            usuario= form.save()
            login(request, usuario)
            return redirect('home')
        else:
            for key, value in form.errors.items():
                messages.error(request, value)
            return render(request, "registro.html", {"form": form})


