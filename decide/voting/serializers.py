from rest_framework import serializers

from .models import Binary_Question, Binary_Question_Option, Binary_Voting, Question, QuestionOption, Voting
from base.serializers import KeySerializer, AuthSerializer


class QuestionOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ('number', 'option')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    options = QuestionOptionSerializer(many=True)
    class Meta:
        model = Question
        fields = ('desc', 'options')


class VotingSerializer(serializers.HyperlinkedModelSerializer):
    question = QuestionSerializer(many=False)
    pub_key = KeySerializer()
    auths = AuthSerializer(many=True)

    class Meta:
        model = Voting
        fields = ('id', 'name', 'desc', 'question', 'start_date',
                  'end_date', 'pub_key', 'auths', 'tally', 'postproc', 'type')


class SimpleVotingSerializer(serializers.HyperlinkedModelSerializer):
    question = QuestionSerializer(many=False)

    class Meta:
        model = Voting
        fields = ('name', 'desc', 'question', 'start_date', 'end_date')


class BinaryQuestionOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Binary_Question_Option
        fields = ('number', 'option')

class BinaryQuestionSerializer(serializers.HyperlinkedModelSerializer):
    options = BinaryQuestionOptionSerializer(many=True)
    class Meta:
        model = Binary_Question
        fields = ('desc', 'options')

class BinaryVotingSerializer(serializers.HyperlinkedModelSerializer):
    question = BinaryQuestionSerializer(many=False)
    pub_key = KeySerializer()
    auths = AuthSerializer(many=True)

    class Meta:
        model = Binary_Voting
        fields = ('id', 'name', 'desc', 'question', 'start_date',
                  'end_date', 'pub_key', 'auths', 'tally', 'postproc', 'type')

class SimpleBinaryVotingSerializer(serializers.HyperlinkedModelSerializer):
    question = BinaryQuestionSerializer(many=False)

    class Meta:
        model = Binary_Voting
        fields = ('name', 'desc', 'question', 'start_date', 'end_date', 'type')