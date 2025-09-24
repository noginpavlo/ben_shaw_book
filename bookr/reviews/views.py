from django.shortcuts import render


def index(request):
    name = "Highlander"
    return render(request, "base.html", {"name": name})
