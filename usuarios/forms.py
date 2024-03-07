from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=250,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Lucas Nadalin'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=250,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua Senha',
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de cadastro',
        required=True,
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Lucas Nadalin',
            }
    )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=250,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: LucasNadalin@zxop.com'
            }
        )
    )
    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=250,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua Senha',
            }
        )
    )
    senha_2 = forms.CharField(
        label='Confirme sua Senha',
        required=True,
        max_length=250,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua Senha',
            }
        )
    )