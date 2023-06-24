from django import forms


class UserForm(forms.Form):
    gen = [
        ("M", "Masculino"),
        ("F", "Femenino")
    ]

    username = forms.CharField(label="Usuario", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Nombre(s)", max_length=90,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido(s)", max_length=90,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", max_length=90,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", max_length=30, min_length=8,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar Contraseña", max_length=30, min_length=8,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    sexo = forms.ChoiceField(label="Sexo", choices=gen, widget=forms.Select(
        attrs={'class': 'form-control demo_select2 historia '}))
    telefono = forms.CharField(label="Teléfono", max_length=15,
                               widget=forms.TextInput(attrs={'class': 'form-control historia'}))
    especialiad = forms.CharField(label="Especialidad", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control historia'}))


