from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from wiki.models import *

@dajaxice_register
def tag_autocomplete(request,term):
	if term.strip()=="":
		tags = []
	else:
		tags = Tag.objects.filter(name__icontains=term)
	return simplejson.dumps([tag.name for tag in tags])
