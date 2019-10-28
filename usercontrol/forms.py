from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(
        label='user',
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Pseudo ou email', 'class': 'form-control'}
            ),
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Mot de passe', 'class': 'form-control'}
            ),
    )


class SignupForm(forms.Form):
    pseudo = forms.CharField(
        label='pseudo',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Pseudo', 'class': 'form-control'}
        ),
    )
    last_name = forms.CharField(
        label='nom',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Nom', 'class':'form-control'}
        ),
    )
    first_name = forms.CharField(
        label='prénom',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Prénom', 'class': 'form-control'}
        ),
    )
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email', 'class': 'form-control'}
        ),
    )
    password = forms.CharField(
        label='password',
        min_length=8,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Mot de passe', 'class': 'form-control'}
        ),
    )
    confirm_pwd = forms.CharField(
        label='confirm_pwd',
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmation du mot de passe',
                'class': 'form-control'
            }
        ),
    )
