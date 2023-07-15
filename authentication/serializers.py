from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField (max_length=70, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=300, min_length=4)
    username = serializers.CharField(max_length=300, min_length=3)

    class Meta:
        model=User
        fields = [
            'username', 'email', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

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
    '''user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
        #return User.objects.create_user(**validated_data)
    def update(self, instance, validate_data):
        instance.email = validate_data.get('email', instance.email)
        instance.password = validate_data.get('password', instance.password)
        instance.save()
        return instance
        

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        label='Username'
    )
    password = serializers.CharField(
        label = 'Password',
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    #https://www.guguweb.com/2022/01/23/django-rest-framework-authentication-the-easy-way/#why-you-should-avoid-jwt-for-django-rest-framework-authentication

    def validate(self,attrs):
        # take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # try to authenticate the user
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                #if we dont have a regular user, raise a Validationerror
                msg= 'Access denied: wrong useername or password.'
                raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = 'Both username and password are required.'
                raise serializers.ValidationError(msg, code='authorization')

            attrs['user'] = user
            return attrs'''


