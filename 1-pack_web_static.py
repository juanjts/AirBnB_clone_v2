#!/usr/bin/python3
"""Fabric script generates a .tgz archive from web_static"""
from fabric.api import local
import time


def do_pack():
    """do_pack prototype to generate an .tgz"""

    local("mkdir -p versions")
    created = (time.strftime("%Y%m%d%H%M%S"))
    tgzfile = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(created))
    if not tgzfile.succeeded:
        return None
    else:
        return "versions/web_static_{}.tgz".format(created)
