from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from wiki.models import *
from wiki.forms import *

urlpatterns = patterns("wiki.views",
	url("^$", "main",name="wiki_main"),
	url("^webcasts/$", "webcasts",name="wiki_webcasts"),

	url("^entry/edit/(?P<entry_id>\d+)/$", "edit_entry",name="wiki_edit_entry"),
	url("^entry/(?P<entry_id>\d+)/$", "view_entry",name="wiki_view_entry"),
	url("^entry/revert/$", "revert_entry",name="wiki_revert_entry"),
	url("^entry/delete/(?P<entry_id>\d+)/$", "delete_entry",name="wiki_delete_entry"),
	url("^entry/new/$", "new_entry",name="wiki_new_entry"),
)

from tagging.views import tagged_object_list

urlpatterns += patterns('',
	url(r'^entry/tag/(?P<tag>[^/]+)/$',
		tagged_object_list,
		dict(queryset_or_model=Entry, paginate_by=10,
		template_object_name='entry'),
		name='entry_tag_detail'),
)
