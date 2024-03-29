from django.db import models
from django.contrib import admin

import tagging
from tagging.models import Tag

import reversion


class Webcast(models.Model):
	link = models.CharField(max_length=500,default="")

class Entry(models.Model):
	body = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	last_edit_date = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=500,default="")
	webcasts = models.ManyToManyField(Webcast)
	class Meta:
		ordering = ["-last_edit_date"]

class EntryAdmin(reversion.VersionAdmin):
	pass
tagging.register(Entry)
admin.site.register(Entry,EntryAdmin)
admin.site.register(Webcast)
