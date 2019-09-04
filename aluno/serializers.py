from rest_framework import serializers
from aluno.models import Aluno

class AlunoSerializer(serializers.ModeSerializer):
    class Meta:
        model = Aluno
