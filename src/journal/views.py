from django.shortcuts import render

from main.models import Request


def show_journal(request):
    all_requests = Request.objects.all()
    context = {"requests": reversed(all_requests)}
    return render(request, "journal/journal.html", context)
