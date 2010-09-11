from django.conf.urls.defaults import *
from tamatarctrl.views import * 

from tamatarctrl.CmdView import CommandView

cmdview = CommandView() 
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^tamatarctrl/', include('tamatarctrl.foo.urls')),
    ('^$', index),
    ('^status/$', status),
    ('^submitstatus/(.*)', submitstatus),
    ('^cmd/(.*)$', cmdview),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
