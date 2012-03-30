from django.http import HttpResponse
from  django.shortcuts import *
from django.core.urlresolvers import reverse

from wiki.models import *
from wiki.forms import *

def main(request):
	"""
		Displays all entries.
	"""
	entries = [(e,None) for e in Entry.objects.all()]
	return render_to_response("wiki/main.html",{"entries":entries},context_instance = RequestContext(request))

def edit_entry(request,entry_id):
	"""
		View for editing an entry specified by entry_id.
	"""
	E = Entry.objects.get(id=entry_id)
	entries = {e:(e,None) for e in Entry.objects.all()}
	if request.method == "POST":
		form = EntryForm(request.POST)
		if form.is_valid():
			E.body = form.cleaned_data['body']
			Tag.objects.update_tags(E,' '.join([Tag.objects.get(id=int(e)).name for e in form.cleaned_data['tags']]))
			E.save()
			entries[E] = (E,None)
			return HttpResponseRedirect(reverse("wiki.views.main"))
	else:
		form = EntryForm() 
		form.initial['body'] = E.body
		entries[E] = (E,form)
		return render_to_response("wiki/main.html",{"form":form,"entries":sorted(entries.values(),key = lambda x: x[0].last_edit_date, reverse=True)},context_instance = RequestContext(request))

def new_entry(request):
	"""
		Creates a new entry and redirects to :view:`wiki.views.main`
	"""
	e = Entry()
	e.body = "###Place your content here..."
	e.save()
	return HttpResponseRedirect(reverse("wiki.views.main"))

def delete_entry(request,entry_id):
	e = Entry.objects.get(id=entry_id)
	e.delete()
	return HttpResponseRedirect(reverse("wiki.views.main"))

def revert_entry(request):
	if request.method == 'GET':
		if 'version_id' in request.GET:
			try:
				version_id = request.GET['version_id']
				from reversion.models import Version
				version = Version.objects.get(id=version_id)
				version.revert()
			except:
				if 'entry_id' in request.GET:
					entry_id = request.GET['entry_id']
					entry = Entry.objects.get(id=entry_id)
					version = reversion.get_for_object(entry).order_by("pk")
					version[0].revert()
	return HttpResponseRedirect(reverse("wiki.views.main"))
