from django import forms


# Форма создания логина и пароля.
class UserForm(forms.Form):
    email = forms.EmailField(label="Введите Email", help_text="Введите имейл",
                             widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    login = forms.CharField(label="Введите логин", max_length=10, help_text="Сюда логин...",
                            widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Введите пароль", max_length=12, help_text="Что-то поумнее 12345 сюда:",
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Введите возраст", max_value=120, help_text="Введите возраст",
                             widget=forms.widgets.NumberInput(attrs={'class': 'form-control'}))

