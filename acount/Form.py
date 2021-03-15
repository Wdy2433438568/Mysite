from django.forms.forms import Form
from django.forms import fields,widgets
from django.forms import forms
from acount import models

class SighForm(Form):
    user = fields.CharField(
        min_length=5,
        max_length=20,
        error_messages={'required':'账号不能为空','min_length':'最少账号要5个字符','max_length':'最多只能20个字符哦'},
        widget=widgets.Input(attrs={'class':'form-control','placeholder':'请输入账号'})
    )

    pwd = fields.CharField(
        min_length=5,
        max_length=25,
        error_messages={'required':'密码不能为空','min_length':'最少密码要5个字符','max_length':'最多只能30个字符哦'},
        widget=widgets.PasswordInput(attrs={'class':'form-control','placeholder':'请输入密码'})

    )
    email = fields.EmailField(
        error_messages={'required':'邮箱不能为空','invalid':'格式错误'},
        widget=widgets.Input(attrs={'class':'form-control','placeholder':'请输入邮箱'})
    )

    sex_list = (
        (1,'男'),
        (2,'女')
    )
    sex = fields.ChoiceField(
        choices=sex_list,
        widget=widgets.Select
    )
    age = fields.IntegerField(min_value=18,
                              error_messages={'required':'年龄不能为空','min_value':'最小要18岁'},
                              widget=widgets.Input(attrs={'class':'form-control','placeholder':'请输入年龄'})
                            )
    def clean_user(self):
        if models.Userinfo.objects.filter(user=self.cleaned_data['user']).count():
            raise forms.ValidationError('账号已存在')
        return self.cleaned_data['user']
    def clean_email(self):
        if models.Userinfo.objects.filter(email=self.cleaned_data['email']).count():
            raise forms.ValidationError('邮箱已存在')
        return self.cleaned_data['email']

class SighupForm(Form):
    user = fields.CharField(
        min_length=5,
        max_length=30,
        error_messages={'required':'账号不能为空','min_length':'最少账号要5个字符','max_length':'最多只能10个字符哦'},
        widget=widgets.Input(attrs={'class':'form-control','placeholder':'请输入账号'})
    )
    pwd = fields.CharField(
        min_length=5,
        max_length=25,
        error_messages={'required':'密码不能为空','min_length':'最少密码要5个字符','max_length':'最多只能30个字符哦'},
        widget=widgets.PasswordInput(attrs={'class':'form-control','placeholder':'请输入密码'})

    )
    def clean(self):
        if  models.Userinfo.objects.filter(user=self.cleaned_data['user'],pwd=self.cleaned_data['pwd']).count():
            return self.cleaned_data
        raise forms.ValidationError('账号密码有错')


class CsighForm(Form):
    user = fields.CharField(
        min_length=5,
        max_length=20,
        error_messages={'required':'账号不能为空','min_length':'最少账号要5个字符','max_length':'最多只能20个字符哦'},
        widget=widgets.Input(attrs={'class':'form-control','placeholder':'请输入账号','style':'pointer-events: none;'})
    )

    pwd = fields.CharField(
        min_length=5,
        max_length=25,
        error_messages={'required':'密码不能为空','min_length':'最少密码要5个字符','max_length':'最多只能30个字符哦'},
        widget=widgets.Input(attrs={'class':'form-control','placeholder':'请输入密码'})

    )
    email = fields.EmailField(
        error_messages={'required':'邮箱不能为空','invalid':'格式错误'},
        widget=widgets.Input(attrs={'class':'form-control','placeholder':'请输入邮箱'})
    )

    sex_list = (
        (1,'男'),
        (2,'女')
    )
    sex = fields.ChoiceField(
        choices=sex_list,
        widget=widgets.Select
    )
    age = fields.IntegerField(min_value=18,
                              error_messages={'required':'年龄不能为空','min_value':'最小要18岁'},
                              widget=widgets.Input(attrs={'class':'form-control','placeholder':'请输入年龄'})
                              )
