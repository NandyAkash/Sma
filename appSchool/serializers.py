from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


from rest_framework.authtoken.models import Token


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    
    
    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ("username", "password")

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return super(RegistrationSerializer, self).create(validated_data)

class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("auth_token",)        