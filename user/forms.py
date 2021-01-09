from django import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='إسم المستخدم',max_length=30)
    email = forms.EmailField(label='البريد الالكتروني')
    first_name = forms.CharField(label='الإسم الأول')
    last_name = forms.CharField(label='الإسم الثاني')
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=6)
    password2 = forms.CharField(label='تأكيد كلمه المرور', widget=forms.PasswordInput(),min_length=6)
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')
    
    def clean_password2(self):
        cd = self.changed_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة.')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم آخر مسجل بهذا الاسم.')
        return cd['username']

