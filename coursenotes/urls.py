from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

from ajax_select import urls as ajax_select_urls

from pinax.apps.account.openid_consumer import PinaxConsumer

from wiki.models import Entry 


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {
        "template": "homepage.html",
    }, name="home"),
	url(r'^admin_tools/', include('admin_tools.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^about/", include("about.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/", include(PinaxConsumer().urls)),
    url(r"^profiles/", include("idios.urls")),
    url(r"^notices/", include("notification.urls")),
    url(r"^announcements/", include("announcements.urls")),
	url(r"^wiki/",include("wiki.urls")),
	url(r'^tinymce/', include('tinymce.urls')),
	url(r'^markitup/', include('markitup.urls')),
	url(r'^admin/lookups/', include(ajax_select_urls)),
	url(r'^hashtags/', include('hashtags.urls')),
	(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
