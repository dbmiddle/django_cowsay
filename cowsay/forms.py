from django import forms


class SubmittedTextForm(forms.Form):
    input_text = forms.CharField(max_length=100)
