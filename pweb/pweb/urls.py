from django.conf.urls import patterns, include, url

from django.contrib import admin
from pweb.API.openAPI import hello

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^gwq/api', hello),
)
