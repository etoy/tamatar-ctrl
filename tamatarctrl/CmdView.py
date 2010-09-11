from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.conf import settings
import time
import simplejson
import socket
import random

class CommandView(object):
    _sock = None

    def __init__(self):
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        except Exception, err:
            pass

    def __call__(self, request, *args, **kwargs):
        rand = random.randint(0,1000)

        data = {'success' : 0, 'random':rand}
        tamatarId=0
        cmd=''
        if 'tamatar' in request.GET:
            tamatarId = int(request.GET['tamatar'])
        if 'cmd' in request.GET:
            cmd = request.GET['cmd']

        if tamatarId is not 0 and len(cmd) > 0:
            dest = ('<broadcast>', 22044)
            if self._sock is not None:
                try:
                    msg = "c:0:%d:%s" % (tamatarId, cmd)
                    self._sock.sendto(msg, dest)
                    time.sleep(0.5)
                    data['cmd'] = msg
                    data['tamatar'] = tamatarId
                    data['success']=1
                    data['sock'] = str(self._sock)
                except Exception, err:
                    data['success']=0
                    data['error'] = err

        r =  HttpResponse(simplejson.dumps(data), mimetype='application/json')
        r['Cache-Control'] = 'no-cache'
        return r
