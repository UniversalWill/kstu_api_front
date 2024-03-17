from django.shortcuts import render, redirect


def index(request):
    if "username" not in request.session:
        return redirect("login")

    context = {"text": "Добро пожаловать!"}
    return render(request, "main/index.html", context)
