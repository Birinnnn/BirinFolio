from django import forms
from projects.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        labels = {
            "text": "Your Comment",
        }
