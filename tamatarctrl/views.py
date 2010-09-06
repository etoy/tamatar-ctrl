from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.conf import settings
import simplejson
import datetime
import glob

def submitstatus(request, args):
    s = ''
    tamatarId = 0
    
    if 'tamatarId' in request.GET:
        s+= request.GET['tamatarId']
        tamatarId = int(request.GET['tamatarId'])
    s+= ','
    if 'ip' in request.GET:
        s+= request.GET['ip']
    s+= ','
    if 'state' in request.GET:
        s+= request.GET['state']
    s+= ','
    if 'power' in request.GET:
        s+= request.GET['power']
    s+= ','
    if 'uptime' in request.GET:
        s+= request.GET['uptime']
    s+= ','
    now = datetime.datetime.now()
    s+= now.strftime("%Y-%m-%d %H:%M:%S")
    filename = "%s/tamatar-%d.txt" % (settings.STATFILEDIR, tamatarId)
    f = open(filename, 'w')
    f.write(s)
    f.close()
    t = get_template('submitstatus.html')
    html = t.render(Context({'status': s}))
    return HttpResponse(html)

def status(request):
    l = glob.glob("%s/*.txt" % (settings.STATFILEDIR))
    data = {'tamatar': []}
    for file in l:
        fp = open(file)
        c = fp.readline()
        if c != '':
            p = c.split(',')
            data['tamatar'].append(p)
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def index(request):
	t = get_template('index.html')
	html = t.render(Context({}))
	return HttpResponse(html)
