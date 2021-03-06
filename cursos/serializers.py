from rest_framework import serializers
from .models import Curso, Avaliacao


class AvalicaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {
                'write_only': True
            }
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )


class CursoSerializer(serializers.ModelSerializer):

    #Nested relaitonship
    avaliacoes = AvalicaoSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
