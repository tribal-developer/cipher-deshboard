from django import forms



class RegisterForm(forms.Form):
    employee_id = forms.CharField( max_length=6)
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput )
    password2 = forms.CharField( widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Passwords do not match.')

        return cleaned_data