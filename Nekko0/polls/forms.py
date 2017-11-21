#!/usr/bin/env python
# encoding: utf-8

import datetime
import re
import markdown

from django import forms

from models import Article, Userinfo


class ArticlePublishForm(forms.Form):
    title = forms.CharField(
        label=u'Article Title',
        max_length=50,
        widget=forms.TextInput(attrs={'class': '', 'placeholder': u'title, add ".html" at the end.'}),
    )

    content = forms.CharField(
        label=u'content',
        min_length=10,
        widget=forms.Textarea(),
    )

    tags = forms.CharField(
        label=u'tags',
        max_length=30,
        widget=forms.TextInput(attrs={'class': '', 'placeholder': u'article Title, split with space.'}),
    )

    def save(self, username, article=None):
        cd = self.cleaned_data
        title = cd['title']
        title_zh = title
        now = datetime.datetime.now()
        content_md = cd['content']
        content_html = markdown.markdown(cd['content'])
        re_title = '<h\d>(.+)</h\d>'
        data = content_html.split('\n')
        for line in data:
            title_info = re.findall(re_title, line)
            if title_info:
                title_zh = title_info[0]
                break
        url = 'article/%s' % (title)
        tags = cd['tags']
        if article:
            article.url = url
            article.title = title
            article.title_zh = title_zh
            article.content_md = content_md
            article.content_html = content_html
            article.tags = tags
            article.updated = now
        else:
            article = Article(
                url=url,
                title=title,
                title_zh=title_zh,
                author=username,
                content_md=content_md,
                content_html=content_html,
                tags=tags,
                views=0,
                created=now,
                updated=now)
        article.save()

class LoginForm(forms.Form):
    email = forms.EmailField(
        label = u'邮箱',
        help_text = u'邮箱登录',
        max_length = 50,
        initial = '',
        widget = forms.TextInput(attrs={'class': 'form-control'}),
    )

    password = forms.CharField(
        label = u'密码',
        help_text = u'请输入密码',
        min_length = 6,
        max_length = 18,
        widget = forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        res = Userinfo.objects.filter(email=email, password=password)
        if (len(res) == 0):
            raise forms.ValidationError(u'邮箱或密码错误')


class RegisterForm(forms.Form):
    username = forms.CharField(
        label = u'昵称',
        help_text = u'昵称可用于登录',
        max_length = 20,
        initial = '',
        widget = forms.TextInput(attrs={'class': 'form-control'}),
    )

    email = forms.EmailField(
        label = u'邮箱',
        help_text = u'可用于找回密码',
        max_length = 50,
        initial = '',
        widget = forms.TextInput(attrs={'class': 'form-control'}),
    )

    password = forms.CharField(
        label = u'密码',
        help_text = u'请输入密码',
        min_length = 6,
        max_length = 18,
        widget = forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    confirm_password = forms.CharField(
        label = u'确认密码',
        min_length = 6,
        max_length = 18,
        widget = forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if ' ' in username or '@' in username:
            raise forms.ValidationError(u'昵称中不能包含@和空格字符')
        res = Userinfo.objects.filter(username=username)
        if (len(res) != 0):
            raise forms.ValidationError(u'此昵称已经被注册，请重新输入')

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        res = Userinfo.objects.filter(email=email)
        if (len(res) != 0):
            raise forms.ValidationError(u'此邮箱已经被注册，请重新输入')

        return email

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(u'两次输入密码不一致，请重新输入')


    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        userinfo = Userinfo(
            username = username,
            password = password,
            email = email,
            sex = "1",
            created_date = datetime.datetime.now(),
            level = "0",
            level_tag = u"无能力者",
            birthday = datetime.datetime.now(),
            introduce = "",
            avatar_url = "")

        userinfo.save()




