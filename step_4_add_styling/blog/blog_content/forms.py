from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField()

