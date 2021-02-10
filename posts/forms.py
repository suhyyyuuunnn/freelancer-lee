from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    _type = forms.ChoiceField(
        widget=forms.RadioSelect,
        label="게시글 종류",
        choices=Post.POST_TYPE,
        required=True
    )

    class Meta:
        model = Post
        fields = ['title', '_type', 'content', 'image']
        labels = {
            'title': '제목',
            'content': '내용',
            'image': '게시글 대표 이미지',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': SummernoteWidget(),
        }