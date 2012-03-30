from django import template
import reversion
register = template.Library()

@register.inclusion_tag("wiki/entry.html",takes_context=True)
def entry(context,e,form=None):
	"""
		Display an entry using markdown, version control, tagging, and mathjax.
	"""
	version_list = reversion.get_for_object(e).order_by("pk")
	return {"entry":e,"form":form,"versions":version_list}

@register.inclusion_tag("wiki/tag.html",takes_context=True)
def tag(context,t):
	"""
		Display a tag that links to a filtered page of entries.
	"""
	return {"tag":t}
