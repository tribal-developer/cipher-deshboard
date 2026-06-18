from django import forms
from .models import CipherRecord
from .models import UserVerification
from django.contrib.auth.models import User





class CipherRecordForm(forms.ModelForm):

    key_file = forms.FileField(required=True)

    class Meta:
        model = CipherRecord
        fields = ['name','agent_name', 'ip_address', 'section']

    def clean_agent_name(self):
        agent_name = self.cleaned_data.get('agent_name')
        if CipherRecord.objects.filter(agent_name=agent_name).exists():
            raise forms.ValidationError( 'This Agent Name Already Exists.')
        return agent_name

    def clean_ip_address(self):
        ip_address = self.cleaned_data.get('ip_address')
        if CipherRecord.objects.filter(ip_address=ip_address).exists():
            raise forms.ValidationError("IP Address Already Exist.")
        return ip_address

    def clean_key_file(self):
        file = self.cleaned_data.get('key_file')
        if not file:
            raise forms.ValidationError('Please upload a file.')

        if not file.name.endswith('.txt'):
            raise forms.ValidationError('Only .txt files allowed.')
        return file
    

class UserVerificationForm(forms.ModelForm):
    employee_id = forms.CharField(required=True)

    class Meta:
        model = UserVerification
        fields = ['employee_id', 'designation', 'section']

    def clean_user_id(self):
        employee_id = self.cleaned_data.get('employee_id')
        if UserVerification.objects.filter(employee_id=employee_id).exists():
            raise forms.ValidationError( 'This User Id or Pr No. Already Exists.')
        return employee_id
    


class EditCipherRecordForm(forms.ModelForm):

    class Meta:
        model = CipherRecord

        fields = [ 'name', 'ip_address', 'section']

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'ip_address': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'section': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }