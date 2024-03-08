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

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome= nome.strip()
            if ' 'in nome:
                raise forms.ValidationError('Não é possivel inserir espaços dentro do Nome de Cadastro')
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas não são iguais, tente novamente.')
            else:
                return senha_2