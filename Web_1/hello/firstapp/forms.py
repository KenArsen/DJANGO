from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя",
                           widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label="Возраст",
                             widget=forms.NumberInput(attrs={"class": "myfield"}))
