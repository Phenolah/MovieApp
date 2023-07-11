from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField (max_length=70, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=300, min_length=4)
    username = serializers.CharField(max_length=300, min_length=3)

    class Meta:
        model=User
        fields = [
            'username', 'email', 'password'
        ]
    def validate(self, attrs):
        email = attrs.get('email')
        username = attrs.get('username')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {
                    'email': ('Email is already in use')
                }
            )
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {
                    'username': ('Hey! looks like this username is taken. '
                                 'Please try another one')
                }
            )
        return super().validate(attrs)
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    def update(self, instance, validate_data):
        instance.email = validate_data.get('email', instance.email)
        instance.password = validate_data.get('password', instance.password)