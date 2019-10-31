from django import forms

class additemsForm(forms.Form):
    ItemName = forms.CharField()
    ItemQuantity = forms.CharField()

