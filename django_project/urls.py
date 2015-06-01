from django.conf.urls import patterns, include, url
from django .conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'glass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^servicios', 'glass.views.servicios', name='servicios'),
    url(r'^detalleservice', 'glass.views.detalleservice', name='detalleservice'),
    url(r'^media/(?P<path>.*)$','glass.views.static.server',{'document_root':settings.MEDIA_ROOT}),
    
)
