from django import forms
from pybo.models import Question, Answer, Comment


class QuestionForm(forms.ModelForm): # ModelForm을 상속받아 모델 폼을 만듦.
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        lables = {
            'content' : '댓글내용',
        }