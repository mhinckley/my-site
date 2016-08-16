from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('to_field','do_field','when','content_type', 'support_link', 'summary')