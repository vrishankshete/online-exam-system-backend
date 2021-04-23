from rest_framework import serializers
from hello.models import Exam_details, Subjective_ques, Objective_ques

class Exam_details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Exam_details
        feilds = ['exam_id', ' subject_id', 'exam_date', 'exam_time']

class Subjective_ques_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subjective_ques
        feilds = ['exam_id', 'ques_text', 'mark']

class Subjective_ques_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subjective_ques
        feilds = ['exam_id', 'ques_text', 'option1', 'option2', 'option3', 'option4', 'correct_ans','mark']  