from django import template
from wiki.models import *
from wiki.forms import *
import reversion
register = template.Library()

@register.inclusion_tag("wiki/entry.html",takes_context=True)
def entry(context,e=None,entry_form=None,webcast_form=WebcastForm()):
	"""
		Display an entry using markdown, version control, tagging, and mathjax.
	"""
	if e==None:
		e = Entry.objects.all().order_by("pk")[0]
	version_list = reversion.get_for_object(e).order_by("pk")
	tag_form = TagForm()
	tag_form.initial['tags'] = [c.pk for c in e.tags]
	return {"entry":e,"entry_form":entry_form,"webcast_form":webcast_form,"tag_form":tag_form,"versions":version_list}

@register.inclusion_tag("wiki/tag.html",takes_context=True)
def tag(context,t):
	"""
		Display a tag that links to a filtered page of entries.
	"""
	return {"tag":t}
