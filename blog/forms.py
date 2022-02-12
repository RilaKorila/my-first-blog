from dataclasses import field
from django import forms
from .models import Post

# tell Django that this form is a ModelForm
class PostForm(forms.ModelForm):
    # tell Django which model should be used to create this form
    class Meta:
        model=Post
        # which fields should end up in our form
        fields = ('title', 'text')