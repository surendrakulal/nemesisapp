from rest_framework import serializers

from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password', 'address')
        extra_kwargs = {
                'password': {'write_only': True},
        }	


    def	save(self):
        users = User(
                    email=self.validated_data['email'],
                    username=self.validated_data['username']
                )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        address = self.validated_data['address']
        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        users.set_password(password)
        users.save()
        return users