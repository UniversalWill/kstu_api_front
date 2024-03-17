import json

import requests
from django.shortcuts import render, redirect
from main.models import Request


def show_notes(request):
    try:
        login = request.session["username"]
        password = request.session["password"]
    except:
        return redirect("login")
    resp = requests.post(
        "http://130.61.172.179:8080/get_journal",
        json={"login": login, "password": password},
    )

    new_request = Request(username=login, response=resp.text)
    new_request.save()
    data = json.loads(resp.json())

    context = {"data": data}
    return render(request, "notes/notes.html", context)
