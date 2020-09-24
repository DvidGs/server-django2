from rest_auth.registration.serializers import RegisterSerializer
#from rest_auth.registration.views import RegisterView
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_auth.serializers import TokenSerializer
from rest_auth.serializers import PasswordResetSerializer
from allauth.account.forms import ResetPasswordForm


class NameRegistrationSerializer(RegisterSerializer):

  name = serializers.CharField(required=True)
  date_of_birth = serializers.IntegerField(required=True)
  gender = serializers.CharField(required=True)
  country = serializers.CharField(required=True)

  def custom_signup(self, request, user):
    user.name = self.validated_data.get('name', '')
    user.date_of_birth = self.validated_data.get('date_of_birth', '')
    user.gender = self.validated_data.get('gender', '')
    user.country = self.validated_data.get('country', '')

    user.save(update_fields=['name'])
    user.save(update_fields=['date_of_birth'])
    user.save(update_fields=['gender'])
    user.save(update_fields=['country'])




class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email','name','date_of_birth','gender','country')


class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')


class PasswordSerializer (PasswordResetSerializer):
    password_reset_form_class = ResetPasswordForm

#class NameRegistrationView(RegisterView):
  # serializer_class = NameRegistrationSerializer