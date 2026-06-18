from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class CipherRecord(models.Model):
    name = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255, unique=True )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    section = models.CharField(max_length=255)
    cipher_key = models.TextField(unique=True)
    created_by = models.ForeignKey( User, on_delete=models.CASCADE )
    uploaded_date = models.DateTimeField(auto_now_add=True)


    

    def masked_key(self):
        key = self.cipher_key
        if len(key) <= 6: 
            return '*' * len(key)

        return f"{key[:3]}******{key[-3:]}"

    def __str__(self):
        return self.agent_name



class UserVerification(models.Model):
    employee_id = models.CharField( max_length=6, validators=[
            RegexValidator(r'^[a-zA-Z0-9]{6}$', 'User ID must contain 6 digits.')], unique=True)

    designation = models.CharField( max_length=10 )
    section = models.CharField( max_length=100)
    is_registered = models.BooleanField( default=False)

    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='authorised_users'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.employee_id)