from rest_framework import serializers

from .models import User #, UserTasks
# Visualizar tudo no front-End
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Visualizar somente um atributo 
# class UserMailSerializer(serializers.modelSerializer):
#     class Meta:
#         model = User
#         fields = ['user_email']

# Visualizar parcialmente
# class UserTaskSerializer(serializers.modelSerializer):
#     class Meta:
#         model = User
#         fields = ['user_nickname','user_task']