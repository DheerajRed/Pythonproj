from django import forms

class InviteForm(forms.Form):
    email = forms.EmailField(label='Invite Email', max_length=100)
