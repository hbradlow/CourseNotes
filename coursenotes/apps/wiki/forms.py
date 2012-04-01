from django import forms
from ajax_select.fields import AutoCompleteSelectMultipleField

from wmd.widgets import MarkDownInput

class EntryForm(forms.Form):
	title = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"Select a title"}))
	body = forms.CharField(widget=MarkDownInput(attrs={"cols":"80","width":"900px"}),label="")

class WebcastForm(forms.Form):
	link = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"Link to video"}))

class TagForm(forms.Form):
	tags = AutoCompleteSelectMultipleField('tag', required=False,label="",widget=forms.TextInput(attrs={"placeholder":"Tags"}))

