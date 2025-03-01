from rest_framework import serializers
from .models import Game #GameGenre



"""class GameGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameGenre
        fields = '__all__'

    class NestedGameSerializer(serializers.ModelSerializer):

        class Meta:
            model = Game
            fields = ['id', 'title', 'image_thumbnail']

    games = NestedGameSerializer(
        many=True, source="game_genres")  # query reversa"""


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'

    """class NestedGameGenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = GameGenre
            fields = '__all__'

    genres = NestedGameGenreSerializer(many=True)"""