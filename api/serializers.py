from rest_auth.registration.serializers import RegisterSerializer
#from rest_auth.registration.views import RegisterView
from rest_framework import serializers
from django.contrib.auth import get_user_model
#from users.models import A1
from rest_auth.serializers import TokenSerializer
from rest_auth.serializers import PasswordResetSerializer
from allauth.account.forms import ResetPasswordForm


class NameRegistrationSerializer(RegisterSerializer):

  name = serializers.CharField(required=True)
  date_of_birth = serializers.CharField(required=True)
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

########################################################
'''class A1RegistrationSerializer(RegisterSerializer):
  id = serializers.IntegerField(required=True)
  category = serializers.CharField(required=True)
  text = serializers.CharField(required=True)

  def custom_a1(self, request, userss):
    userss.id = self.validated_data.get('id', '')
    userss.category = self.validated_data.get('category', '')
    userss.text = self.validated_data.get('text', '')

    userss.save(update_fields=['id'])
    userss.save(update_fields=['category'])
    userss.save(update_fields=['text'])'''
##########################################################

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        #model = A1
        fields = ('id', 'email','name','date_of_birth','gender','country')
        #fields = ('id', 'category', 'text')


class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')


class PasswordSerializer (PasswordResetSerializer):
    password_reset_form_class = ResetPasswordForm

#class NameRegistrationView(RegisterView):
  # serializer_class = NameRegistrationSerializer