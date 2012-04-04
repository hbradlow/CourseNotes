from django.http import HttpResponse
from  django.shortcuts import *
from django.core.urlresolvers import reverse

from wiki.models import *
from wiki.forms import *

def main(request):
	"""
		Displays all entries.
	"""
	entries = [(e,None,None) for e in Entry.objects.all()]
	return render_to_response("wiki/main.html",{"entries":entries},context_instance = RequestContext(request))

def view_entry(request,entry_id):
	try:
		e = Entry.objects.get(id=entry_id)
		return render_to_response("wiki/main.html",{"entries":[(e,None,None)]},context_instance = RequestContext(request))
	except:
		return HttpResponseRedirect(reverse("wiki.views.main"))
def edit_entry(request,entry_id):
	"""
		View for editing an entry specified by entry_id.
	"""
	E = Entry.objects.get(id=entry_id)
	if request.method == "POST":
		entry_form = EntryForm(request.POST)
		done = False
		if entry_form.is_valid():
			E.body = entry_form.cleaned_data['body']
			E.title = entry_form.cleaned_data['title']
			E.save()
			done = True
		webcast_form = WebcastForm(request.POST)
		if webcast_form.is_valid():
			w = Webcast()
			w.link = webcast_form.cleaned_data['link']
			w.save()
			E.webcasts.add(w)
			E.save()
			done = True
		if done:
			return HttpResponseRedirect(reverse("wiki.views.main"))
		return render_to_response("wiki/entry_form.html",{"entry_form":entry_form,"webcast_form":webcast_form,"entry":E},context_instance = RequestContext(request))
	else:
		entry_form = EntryForm() 
		entry_form.initial['body'] = E.body
		entry_form.initial['title'] = E.title

		return render_to_response("wiki/entry_form.html",{"entry_form":entry_form,"entry":E},context_instance = RequestContext(request))

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



def webcasts(request):
	return render_to_response("wiki/webcasts.html",context_instance = RequestContext(request))
