import requests
from django.shortcuts import render, redirect

from .forms import LoginForm


def show_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            resp = requests.post(
                "http://130.61.172.179:8080/get_journal",
                json={"login": username, "password": password},
            )
            if resp.status_code is 200:
                request.session["username"] = username
                request.session["password"] = password
                return redirect("index")
            else:
                return redirect("login")
                return render(request, "login.html", {"form": form, "error": True})
    else:
        form = LoginForm()

    context = {"form": form}
    return render(request, "login/login.html", context)
