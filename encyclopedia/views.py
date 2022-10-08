from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    page = util.get_entry(name)
    if page != None:
        markdowner = Markdown()
        return render(request, )

