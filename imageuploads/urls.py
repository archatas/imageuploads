# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from ajaxuploader.views import AjaxFileUploader

uploader = AjaxFileUploader()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^helper/ajax-upload/$', uploader, name="ajax_uploader"),
    url(r'^$', 'images.views.image_list', name='image_list'),
    url(r'^images/(?P<image_id>\d*)/$', 'images.views.image_upload', name='change_image'),
    url(r'^images/add/$', 'images.views.image_upload', name='add_image'),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}, name="media_url"),
) + urlpatterns