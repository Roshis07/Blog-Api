from django.contrib.auth.models import User
from rest_framework import serializers  

class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type':'password',} ,write_only=True)
    class Meta:
        model=User
        fields=['username', 'password', 'email','password_confirmation']
        extra_kwargs={
            'password':{'write_only':True}}
 



    def save(self):
        password=self.validated_data['password']
        password_confirmation=self.validated_data['password_confirmation']

        if password_confirmation != password:
            raise serializers.ValidationError({'password needs to be same'})
        email = self.validated_data['email']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'This email already exists'})
        account=User(email=self.validated_data['email'], username=self.validated_data['username'])
        
        account.set_password(password)
        account.save()
        return account