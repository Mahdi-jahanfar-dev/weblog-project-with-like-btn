from django import forms

class ContactForm(forms.Form):
    name = forms.TextInput(attrs={'placeholder': 'name'})
    last_name = forms.TextInput(attrs={'placeholder': 'last_name'})
    text = forms.TextInput(attrs={'placeholder': 'enter your text'})
