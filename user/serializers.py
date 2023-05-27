from rest_framework import serializers
from .models import Profile
from rest_framework.validators import UniqueValidator
class ProfileSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=Profile.objects.all())]
        )
    password = serializers.CharField(
        required=True,
        write_only=True,
        )

    class Meta:
        model = Profile
        exclude = [
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
            "is_superuser",
            "is_active",
        ]
    
    def validate(self, attrs):
        if attrs.get("password", False):
            from django.contrib.auth.password_validation import validate_password
            from django.contrib.auth.hashers import make_password
            password = attrs["password"]
            validate_password(password)
            attrs.update({"password":make_password(password)})
        return super().validate(attrs)
    




from dj_rest_auth.serializers import TokenSerializer

class ProfileTokenSerializer(TokenSerializer):

    user = ProfileSerializer()

    class Meta(TokenSerializer.Meta):
        fields= ('key', 'user')

