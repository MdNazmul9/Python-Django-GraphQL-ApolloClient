from dataclasses import field
import graphene
from graphene_django import DjangoObjectType
from .models import Question
class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "question_text")

class Query(graphene.ObjectType):
    questions = graphene.List(QuestionType)
    question_by_id = graphene.Field(QuestionType, id=graphene.Int())

    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()

    def resolve_question_by_id(self, info, id):
        return Question.objects.get(pk=id)


schema = graphene.Schema(query=Query)