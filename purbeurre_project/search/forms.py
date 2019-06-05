from django import forms

class SearchForm(forms.Form):
    research = forms.CharField(
        label='food',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Rechercher', 'class': 'form-control'}),
    )
