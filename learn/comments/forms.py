from django import forms
from .models import Comments


class CommentForm(forms.Form):
    content_type = forms.CharField()
    object_id = forms.IntegerField()
    content = forms.CharField(widget=forms.Textarea)
    # class Meta:
        # model = Comments
        #  fields = ['content']
