from django import forms

class DocumentForm(forms.Form):
    file = forms.FileField()
    title = forms.CharField(max_length = 50)
  