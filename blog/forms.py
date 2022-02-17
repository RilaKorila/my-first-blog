from django import forms
from .models import Comment, Post

# tell Django that this form is a ModelForm
class PostForm(forms.ModelForm):
    # tell Django which model should be used to create this form
    class Meta:
        model = Post
        # which fields should end up in our form
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)