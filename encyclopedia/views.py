from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if title in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "contents": util.get_entry(title)
        })
    else: #give error message
        return render(request, "encyclopedia/entry.html", {
            "title": title.capitalize()
        })
