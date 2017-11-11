# _*_ coding:utf-8 _*_
__author__ = 'admin'
from django import forms

from operation.models import UserAsk
import re

'''
class UserAskForm(forms.Form):
    name = forms.CharField(required=True,min_length=2,max_length=20)
    phone = forms.CharField(required=True,min_length=11,max_length=11)
    course_name = forms.CharField(required=True,min_length=5,max_length=50)
'''


class UserAskForm(forms.ModelForm):
    '''可以添加字段my_field = forms.CharField()'''
    class Meta:
        model = UserAsk
        '''继承model字段'''
        fields = ['name','mobile','course_name']

    def clean_mobile(self):
        '''验证手机号码是否合法'''
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法",code="mobile_invalid")