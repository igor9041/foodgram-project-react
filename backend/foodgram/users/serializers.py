from djoser.serializers import UserSerializer
from rest_framework import serializers

from users.models import CustomUser, Follow



class UserRegistration(UserSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'username', 'first_name', 'last_name')


class CustomUserSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField()
    
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
        )
        
    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        return Follow.objects.filter(
            user=request.user,
            author=obj
        ).exists()


# class RecipeSerializer(serializers.ModelSerializer):
  
#     class Meta:
#         model = Recipe
#         fields = ('id', 'name', 'image', 'cooking_time',)


# class SubscriptionListSerializer(CustomUserSerializer):
#     recipes = serializers.SerializerMethodField()
#     recipes_count = serializers.SerializerMethodField()

#     class Meta:
#         model = CustomUser
#         fields = (
#             'email', 'id', 'username', 'first_name', 'last_name',
#             'is_subscribed', 'recipes', 'recipes_count',
#         )

#     def get_recipes(self, obj):
#         recipes_limit = (
#             self.context['request'].query_params.get('recipes_limit')
#         )
#         if recipes_limit is None:
#             recipes = obj.recipes.all()
#         else:
#             recipes = obj.recipes.all()[:int(recipes_limit)]
#         return RecipeSerializer(recipes, many=True, read_only=True).data

    # def get_recipes_count(self, obj):
    #     return obj.recipes.count()