from django.db.models import Q
from django.utils.html import escape
from tagging.models import Tag
from ajax_select import LookupChannel

class TagLookup(LookupChannel):
	model = Tag 
	def get_query(self,q,request):
		return Tag.objects.filter(Q(name__icontains=q)).order_by('name')
	
	def get_result(self,obj):
		return obj.name
	
	def format_match(self,obj):
		return self.format_item_display(obj)
	
	def format_item_display(self,obj):
		return u"%s" % (escape(obj.name),)
