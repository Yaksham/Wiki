from django.shortcuts import render
from markdown2 import Markdown
from django.shortcuts import redirect
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    page = util.get_entry(name)
    if page is not None:
        markdowner = Markdown()
        content = markdowner.convert(page)
    else:
        content = "<h1>Page does not exist.</h1>"
        name = "Error"
    return render(request, "encyclopedia/entry.html", {
            "content": content,
            "name": name
        })

def search(request):
    query = request.GET.get("q")
    page = util.get_entry(query)
    if page is not None:
        return redirect("entry", name=query)
    else:
        entries = util.list_entries()
        matches = [e for e in entries if query.lower() in e.lower()]
        if not matches:
            heading = "<h2>No reuslts found.</h2>"
        else:
            heading = "<h2>Did you mean:</h2>"
        return render(request, "encyclopedia/search.html", {
            "list": matches,
            "heading": heading
        })

def new(request):
    if request.method == 'GET':
        form = True
        return render(request, "encyclopedia/new.html", {
            "form": form
        })
    title = request.POST.get("title")
    entries = util.list_entries()
    if title not in entries:
        util.save_entry(title, request.POST.get("data"))
        return redirect("entry", name=title)
    else:
        form = False
        return render(request, "encyclopedia/new.html", {
            "form": form,
            "title": title
        })

