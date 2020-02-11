# from rest_framework import serializers, Rating
from rest_framework.serializers import ModelSerializer
from ratings.models import Rating


# the data format for the json api page
class Rating_Serializers(ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'happy',
            'info',
            'housing',
            'schools',
            'police',
            'streets',
            'events',
        ]
