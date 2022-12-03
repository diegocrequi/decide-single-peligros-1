from rest_framework import serializers
from .models import Question, BinaryQuestion
from .models import QuestionOption, BinaryQuestionOption
from .models import Voting, BinaryVoting
from base.serializers import KeySerializer, AuthSerializer


class QuestionOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ('number', 'option')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    options = QuestionOptionSerializer(many=True)
    class Meta:
        model = Question
        fields = ('desc', 'tipo', 'options')


class VotingSerializer(serializers.HyperlinkedModelSerializer):
    question = QuestionSerializer(many=False)
    pub_key = KeySerializer()
    auths = AuthSerializer(many=True)

    class Meta:
        model = Voting
        fields = ('id', 'name', 'desc', 'question', 'start_date',
                  'end_date', 'pub_key', 'auths', 'tally', 'postproc')


class SimpleVotingSerializer(serializers.HyperlinkedModelSerializer):
    question = QuestionSerializer(many=False)

    class Meta:
        model = Voting
        fields = ('name', 'desc', 'question', 'start_date', 'end_date')


#CODIGO DE VOTACIONES BINARIAS

class BinaryQuestionOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BinaryQuestionOption
        fields = ('number', 'option')

class BinaryQuestionSerializer(serializers.HyperlinkedModelSerializer):
    options = BinaryQuestionOptionSerializer(many=True)
    class Meta:
        model = BinaryQuestion
        fields = ('desc', 'options')

class BinaryVotingSerializer(serializers.HyperlinkedModelSerializer):
    question = BinaryQuestionSerializer(many=False)
    pub_key = KeySerializer()
    auths = AuthSerializer(many=True)

    class Meta:
        model = BinaryVoting
        fields = ('id', 'name', 'desc', 'question', 'start_date',
                  'end_date', 'pub_key', 'auths', 'tally', 'postproc', 'type')

class SimpleBinaryVotingSerializer(serializers.HyperlinkedModelSerializer):
    question = BinaryQuestionSerializer(many=False)

    class Meta:
        model = BinaryVoting
        fields = ('name', 'desc', 'question', 'start_date', 'end_date', 'type')
