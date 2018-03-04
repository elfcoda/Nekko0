#!/usr/bin/env python
# encoding: utf-8

import datetime
# import re
import pickle

from django import forms

from .models import Article, Userinfo, SingleMsgBoard


class ArticlePublishForm(forms.Form):
    title = forms.CharField(
        label=u'Article Title',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'title'}),
    )

    content = forms.CharField(
        label=u'content',
        min_length=10,
        widget=forms.Textarea(attrs={'class': 'form-control half', 'id': 'content'}),
    )

    tags = forms.CharField(
        label=u'tags',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'split with space.'}),
    )

    def save(self, username, article=None):
        cd = self.cleaned_data
        title = cd['title']
        # title_zh = title
        now = datetime.datetime.now()
        # content_md = cd['content']
        content_html = cd['content']
        # re_title = '<h\d>(.+)</h\d>'
        # data = content_html.split('\n')
        # for line in data:
        #     title_info = re.findall(re_title, line)
        #     if title_info:
        #         title_zh = title_info[0]
        #         break
        # url = 'article/%s' % (title)
        tags = cd['tags']
        if article:
            # article.url = url
            article.title = title
            # article.title_zh = title_zh
            # article.content_md = content_md
            article.content_html = content_html
            article.tags = tags
            article.updated = now
        else:
            article = Article(
                # url=url,
                title=title,
                # title_zh=title_zh,
                author=username,
                # content_md=content_md,
                content_html=content_html,
                tags=tags,
                views=0,
                created=now,
                updated=now)
        article.save()

class LoginForm(forms.Form):
    email = forms.EmailField(
        required = False,
        label = u'邮箱',
        help_text = u'邮箱登录',
        max_length = 50,
        initial = '',
        widget = forms.TextInput(attrs={'class': 'form-control my-form-control form-control-color'}),
    )

    password = forms.CharField(
        required = False,
        label = u'密码',
        help_text = u'请输入密码',
        max_length = 20,
        widget = forms.PasswordInput(attrs={'class': 'form-control my-form-control form-control-color'}),
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if email == "" or email is None:
            raise forms.ValidationError('Empty email.')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == "" or password is None:
            raise forms.ValidationError('Empty Password.')
        return password


    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        res = Userinfo.objects.filter(email=email, password=password)
        if (len(res) == 0 and (not (password == "" or password is None))):
            raise forms.ValidationError(u'Error email or password.')


class RegisterForm(forms.Form):
    username = forms.CharField(
        required = False,
        label = u'昵称',
        help_text = u'',
        max_length = 20,
        initial = '',
        widget = forms.TextInput(attrs={'class': 'form-control form-control-color'}),
    )

    sex = forms.CharField(
        required = False,
        label = u'性别',
        help_text = u'翻译君已阵亡',
        initial = '1',
        widget = forms.TextInput(attrs={'class': 'form-control select-hidden', 'id': 'form-sex-hidden-text'}),
    )

    email = forms.EmailField(
        required = False,
        label = u'邮箱',
        help_text = u'用于找回密码与登录',
        max_length = 50,
        initial = '',
        widget = forms.TextInput(attrs={'class': 'form-control form-control-color'}),
    )

    password = forms.CharField(
        required = False,
        label = u'密码',
        help_text = u'请输入密码',
        min_length = 6,
        max_length = 18,
        widget = forms.PasswordInput(attrs={'class': 'form-control form-control-color'}),
    )

    confirm_password = forms.CharField(
        required = False,
        label = u'确认密码',
        min_length = 6,
        max_length = 18,
        widget = forms.PasswordInput(attrs={'class': 'form-control form-control-color'}),
    )



    def clean_username(self):
        username = self.cleaned_data['username']
        if username == "" or username is None:
            raise forms.ValidationError('Empty username.')
        if ' ' in username or '@' in username:
            raise forms.ValidationError('" " and "@" are invalid.')
        res = Userinfo.objects.filter(username=username)
        if (len(res) != 0):
            raise forms.ValidationError(u'Nickname has been registered.')

        return username

    def clean_sex(self):
        sex = self.cleaned_data['sex']
        if sex == "" or sex is None:
            raise forms.ValidationError('Empty sex.')
        if not (sex == "1" or sex == "2" or sex == "3" or sex == "4" or sex == "5" or sex == "6" or sex == "7" or sex == "8" or sex == "9" or sex == "10" or sex == "11" or sex == "12"):
            raise forms.ValidationError('Code eror!')

        return sex

    def clean_email(self):
        email = self.cleaned_data['email']
        if email == "" or email is None:
            raise forms.ValidationError('Empty email.')
        res = Userinfo.objects.filter(email=email)
        if (len(res) != 0):
            raise forms.ValidationError(u'Email has been registered.')

        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == "" or password is None:
            raise forms.ValidationError('Empty password.')

        return password


    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        if confirm_password == "" or confirm_password is None:
            raise forms.ValidationError('Empty confirm_password.')

        return confirm_password

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('Password error.')


    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        sex = self.cleaned_data['sex']
        userinfo = Userinfo(
            username = username,
            password = password,
            email = email,
            sex = sex,
            created_date = datetime.datetime.now(),
            com_power = 0,
            level_tag = u"超能力者",
            birthday = datetime.datetime.now(),
            introduce = "",
            avatar_url = "")

        userinfo.save()

class UploadAvatarForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField(
        required = False
    )
    def save(self):
        pass

class MsgBoardForm(forms.Form):
    content = forms.CharField(
        required = False,
        label = u'',
        help_text = u'',
        max_length = 2000,
        initial = '',
        widget = forms.Textarea(attrs={'class': 'form-control form-comment-margin-top', 'name':'reply-msg'}),
    )

    def clean_content(self):
        content = self.cleaned_data['content']
        if content == "" or content is None:
            # print "Empty"
            raise forms.ValidationError('Empty content.')

        # print "Not Empty"
        return content

    # 已弃用，改用Ajax，见AddOrReplyMsg
    # commentId: message id in the model
    def save(self, userId, iArticleId, commentId, replyToName):
        if userId == -1:
            return
        # 第二个参数如果之后要加字段可以用来序列化数据
        # 目前的意义是 是否未删除
        # 评论
        if commentId == -1:
            content = self.cleaned_data['content']
            msg_list = [[userId, 1, str(datetime.datetime.now()), content, set(), replyToName]]
            sMsgList = pickle.dumps(msg_list)
            iArticleId = iArticleId

            single_msg_board = SingleMsgBoard(
                article_id = iArticleId,
                msg_pickle_str = sMsgList
            )
            single_msg_board.save()

        # 回复...
        else:
            content = self.cleaned_data['content']
            reply_item = [userId, 1, str(datetime.datetime.now()), content, set(), replyToName]
            comment_msg = SingleMsgBoard.objects.get(id=commentId)
            # print comment_msg
            list_item = pickle.loads(comment_msg.msg_pickle_str)
            # print list_item
            list_item.append(reply_item)
            # print list_item
            sMsgList = pickle.dumps(list_item)
            comment_msg.msg_pickle_str = sMsgList
            comment_msg.save()




