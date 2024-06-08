from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, widget={
        'placeholder': 'Enter your name'
    })
    last_name = forms.CharField(max_length=50, required=True, widget={
        'placeholder': 'enter your last name'
    })
    text = forms.CharField(max_length=200, required=True, widget={
        'placeholder': 'enter your text'
    })