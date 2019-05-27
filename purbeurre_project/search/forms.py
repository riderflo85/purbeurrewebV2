from django import forms

class SearchForm(forms.Form):
    research = forms.CharField(
        label='food',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Rechercher', 'class': 'form-control'}),
    )

# class LoginForm(forms.Form):
#     user = forms.CharField(
#         label='user',
#         max_length=100,
#         widget=forms.TextInput(
#             attrs={'placeholder': 'Pseudo ou email', 'class': 'form-control'}
#             ),
#     )