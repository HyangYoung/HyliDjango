from django import forms

class ContactForm(forms.Form):
    name = forms.Charfield(max_legnth=255)
    phone =
    email = forms.EmailField()
    content = forms.Text