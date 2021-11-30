from django.shortcuts import render
from markdown2 import markdown
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
            "contents": markdown(util.get_entry(entry))} )

    # else give error message
    return render(request, "encyclopedia/error.html", {
        "page": f"wiki/{title}",
        "error": "page could not be found"
    })

def search(request):
    title = request.GET["q"]
    # if title corresponds to an existing page, render it
    if title.upper() in map(lambda x: x.upper(), util.list_entries()):
        return entry(request, title)
    else:
        return results(request, title)

def results(request, title):
    results = []
    for entry in util.list_entries():
        if title.upper() in entry.upper():
            results.append(entry)

    return render(request, "encyclopedia/results.html", {
        "title": title,
        "results": results
    })
    
def new_page(request):
    try:
        title = request.GET["title"]
        print(util.list_entries(), "hoi")
        if title.upper() in map(lambda x: x.upper(), util.list_entries()):
            return render(request, "encyclopedia/error.html", {
                "page": f"wiki/{title}",
                "error": "page already exists"
                })
        content = request.GET["new_content"]
        print(content)
        util.save_entry(title, content)
        return entry(request, title)
    except:
        return render (request, "encyclopedia/new_page.html", {
    })
    