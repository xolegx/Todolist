from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from first.models import User

class PasswordField(serializers.CharField):
    def __init__(self, **kwargs):
        kwargs['style'] = {"input_type": 'password'}
        kwargs.setdefault('write_only', True)
        super().__init__(**kwargs)
        self.validators.append(validate_password)
class CreateUserSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)
    password_repeate = PasswordField(required=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'password_repeate')
    def validate(self, attrs: dict):
        if attrs['password'] != attrs['password_repeate']:
            raise ValueError('')
        return attrs