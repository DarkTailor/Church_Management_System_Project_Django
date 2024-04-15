from django import forms

from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'surname', 'category', 'birthday', 'email']

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)



