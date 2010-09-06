#!/usr/bin/python
import sys, os
sys.path.append("/home/root/tamatar-ctrl/")
import tamatarctrl
os.environ['DJANGO_SETTINGS_MODULE'] = "tamatarctrl.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
