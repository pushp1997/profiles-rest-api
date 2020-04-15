from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile  # Make serializer to point to UserProfile model
        # List of fields in our model that we want manage through our serializer
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,  # Making it usable for only creating and updating
                # This is just for the browsable api to display *s while typing password
                'style': {'input_type': 'password'}
            }
        }

    # By default model serializer allows us to create simple objects in the database, to resolve this
    # we need to override create() of the object manager to create the object using create_user()
    # such that the password gets hashed instead of clear text.
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
