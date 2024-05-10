from django.contrib.auth.models import User
# from recipe import serializers
from recipe.models import recipe,review
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=recipe
        fields=['id','recipe_name','recipe_ingredients','instructions','cuisine','meal_type']



class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField()    #write_only=True--->Rest apiyill hide cheyyan
    class Meta:
        model=User
        fields=['username','password']

    def create(self, validated_data):
        user=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])

        user.save()
        return user

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=review
        fields=['recipe_name','user','rating','comments']


