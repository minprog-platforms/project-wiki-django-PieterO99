from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    for entry in util.list_entries():
        # if title corresponds to an existing page, render it.
        if title.upper() == entry.upper():
            return render(request, "encyclopedia/entry.html", {
            "title": entry,
            "contents": util.get_entry(entry) })

    # else give error message
    return render(request, "encyclopedia/error.html", {
        "page": f"wiki/{title}"
    })

def search(request):
    title = request.GET["q"]
    return entry(request, title)
    
