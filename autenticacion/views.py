from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
class VRegistro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request, 'registro.html', {'form':form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect()
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'registro.html', {'form':form})


