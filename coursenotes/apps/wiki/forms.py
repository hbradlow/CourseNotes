from django import forms
from ajax_select.fields import AutoCompleteSelectMultipleField

from wmd.widgets import MarkDownInput

class EntryForm(forms.Form):
	title = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"Select a title"}))
	#tags = AutoCompleteSelectMultipleField('tag', required=False, help_text=None,label="")
	#tags = forms.CharField(required=False,label="",widget=forms.TextInput(attrs={"placeholder":"*TODO* Tag this entry..."}))
	body = forms.CharField(widget=MarkDownInput(attrs={"cols":"80","width":"900px"}),label="")


