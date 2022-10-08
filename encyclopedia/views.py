from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    # name = name.capitalize()
    page = util.get_entry(name)
    if page != None:
        markdowner = Markdown()
        return render(request, "encyclopedia/entry.html", {
            "content": markdowner.convert(page),
            "name": name
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "content": "<h1>Page does not exist.</h1>",
            "name": "Error"
        })