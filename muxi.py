from os import listdir
from os.path import expanduser
import re


ymlregex = re.compile(r"\.yml$")


def make_item(item):
    return """<item uid="{0}" arg="{0}" autocomplete="{0}">
    <title>{0}</title>
    <subtitle>mux {0}</subtitle>
    <icon>folder.icns</icon>
</item>""".format(ymlregex.sub("", item))


def mux(query):
    projects = listdir(expanduser("~/.tmuxinator"))
    items = filter(lambda item: item.startswith(query), projects)

    print """<?xml version="1.0"?>
<items>
    %s
</items>""" % map(make_item, items)
