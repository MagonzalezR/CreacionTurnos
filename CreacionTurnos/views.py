from django.shortcuts import render

def viewUsers(request):
    ctx={"name":"Jaime"}
    return render(request, "user.html", ctx)