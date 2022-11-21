from django.shortcuts import render, redirect
from django.views.generic import View
from ModelView.formsUser import AdminFormCreateUser
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView

class URegistration(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = AdminFormCreateUser()
        return render(request, "registration.html", {"form": form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form =AdminFormCreateUser(request.POST, request.FILES)
        if form.is_valid():
            
            user= form.save()
            login(request, user)
            return redirect('home')
        else:
            for key, value in form.errors.items():
                messages.error(request, value)
            return render(request, "registration.html", {"form": form})

class UserLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(UserLoginView, self).get(request=request, *args, **kwargs)

