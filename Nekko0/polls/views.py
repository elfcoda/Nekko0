# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import time
import pickle
import logging
from PIL import Image
import threading

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from django.views.generic.list import ListView
from .models import Article, SingleMsgBoard, Userinfo, LikeMeData
from django.urls import reverse, reverse_lazy # python3
# from django.core.urlresolvers import reverse, reverse_lazy  # python2
from django.views import generic
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from .forms import ArticlePublishForm, RegisterForm, LoginForm, MsgBoardForm, UploadAvatarForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import base64
import random
import datetime
from Nekko0 import consumers

from django.core.mail import send_mail


SHOW_CONTENT_SPLIT = "#####"
COM_POWER_RATE = 100
EMAIL_SUBJECT = u'这里是来自http://eientei.moe/的邮件!!'
MY_EMAIL_ADDR = "707935952@qq.com"

# init logging
logger = logging.getLogger('MyLog')
logger.setLevel(logging.INFO)

# fh = logging.FileHandler('/info.log')
fh = logging.FileHandler('/root/nekko/Nekko0/Nekko0/polls/templates/polls/log.html')
fh.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)
# logger.info('233')

def writeLoggerData(request, cusData):
    s = request.META['REMOTE_ADDR'] + '| ' +  request.META['REMOTE_HOST'] + '| ';

    try:
        userId = request.session['userId']
    except:
        userId = 0

    s += (str(userId) + '| ')
    if userId == 0:
        s += ('NoName' + '| ')
    else:
        s += (Userinfo.objects.get(id=userId).username + '| ')

    s += (str(cusData) + '| ')
    s += request.META['HTTP_USER_AGENT']

    s += "\n<br>"

    logger.info(s)

    return s


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
    response = "you are looking at the res of question %s."
    return HttpResponse(response % question_id)


## class
class IndexView(generic.ListView):
    template_name = 'polls/msgboard.html'
    # template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:3]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

class CodeListView(ListView):
    template_name = 'polls/code.html'

    def get_queryset(self, **kwargs):
        object_list = Article.objects.filter(tags="code").order_by(F('created').desc())
        paginator = Paginator(object_list, 5)
        page = self.kwargs.get('page')
        if page is None:
            page = 1
        writeLoggerData(self.request, "CodeList"+str(page))
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        for ob in object_list:
            # 查找展示部分
            ob_show = ob.content_html.split(SHOW_CONTENT_SPLIT)
            if len(ob_show) == 2:
                ob.content_html = ob_show[0]

            ob.tags = ob.tags.split()
            ob.created = str(ob.created).split(' ')[0]
            ob.updated = str(ob.updated).split(' ')[0]
            date_list = ob.created.split(' ')[0].split('-')
            ob.cr_mon = date_list[1]
            if ob.cr_mon[0] == '0':
                ob.cr_mon = ob.cr_mon[1]
            ob.cr_day = date_list[2]
            if ob.cr_day[0] == '0':
                ob.cr_day = ob.cr_day[1]

        ret_list = []
        pageInfo = [int(page), int(paginator.num_pages)]
        # print int(page)
        # print int(paginator.num_pages)
        ret_list.append(pageInfo)
        ret_list.append(object_list)
        return ret_list



class ArticleListView(ListView):
    # template_name = 'polls/blog_index.html'
    template_name = 'polls/main.html'

    def get_queryset(self, **kwargs):
        object_list = Article.objects.all().order_by(F('created').desc())
        paginator = Paginator(object_list, 7)
        page = self.kwargs.get('page')
        if page is None:
            page = 1
        writeLoggerData(self.request, "ArticleList"+str(page))
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        for ob in object_list:
            # 查找展示部分
            ob_show = ob.content_html.split(SHOW_CONTENT_SPLIT)
            if len(ob_show) == 2:
                ob.content_html = ob_show[0]

            ob.tags = ob.tags.split()
            ob.created = str(ob.created).split(' ')[0]
            ob.updated = str(ob.updated).split(' ')[0]
            date_list = ob.created.split(' ')[0].split('-')
            ob.cr_mon = date_list[1]
            if ob.cr_mon[0] == '0':
                ob.cr_mon = ob.cr_mon[1]
            ob.cr_day = date_list[2]
            if ob.cr_day[0] == '0':
                ob.cr_day = ob.cr_day[1]

        ret_list = []
        pageInfo = [int(page), int(paginator.num_pages)]
        # print int(page)
        # print int(paginator.num_pages)
        ret_list.append(pageInfo)
        ret_list.append(object_list)
        return ret_list

class ArticlePublishView(FormView):
    template_name = 'polls/article_publish.html'
    form_class = ArticlePublishForm
    success_url = reverse_lazy('polls:blog_index')

    def form_valid(self, form):
        userId = self.request.session['userId']
        userName = Userinfo.objects.get(id=userId).username
        form.save(userName)
        return super(ArticlePublishView, self).form_valid(form)


class ResourceView(DetailView):
    template_name = 'polls/resource.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "Resource")
        return None

class AnotherWorldView(DetailView):
    template_name = 'polls/anotherworld.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "AnotherWorld")
        return None

class NewIndexView(DetailView):
    template_name = 'polls/index.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "NewIndex")
        return None

class ResumeView(DetailView):
    template_name = 'polls/resume.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "Resume")
        return None

class FriendsView(DetailView):
    template_name = 'polls/friends.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "Friends")
        return None

class OurStoryView(DetailView):
    template_name = 'polls/ourstory.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "OurStory")
        return None
class OurFutureView(DetailView):
    template_name = 'polls/ourfuture.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "OurFuture")
        return None

class OurILoveYouView(DetailView):
    template_name = 'polls/ourmemory_i_love_you.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "OurILoveYou")
        return None
class OurTODOView(DetailView):
    template_name = 'polls/ourtodo.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "OurTODO")
        return None
class OurStartView(DetailView):
    template_name = 'polls/ourstart.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "OurStart")
        return None
class ConnectView(DetailView):
    template_name = 'polls/connect.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "Connect")
        return None
class OurFlowerAndLightView(DetailView):
    template_name = 'polls/ourmemory_flower_and_light.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "OurFlowerAndLight")
        return None
class OurStarAndAfarView(DetailView):
    template_name = 'polls/ourmemory_star_and_afar.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "OurStarAndAfar")
        return None
class OurMemoryView(DetailView):
    template_name = 'polls/ourmemory.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "OurMemory")
        return None
class OurTogetherView(DetailView):
    template_name = 'polls/ourtogether.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "OurTogether")
        return None
class OurBlessingView(DetailView):
    template_name = 'polls/ourblessing.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "OurBlessing")
        return None
class OurEdenView(DetailView):
    template_name = 'polls/oureden.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "OurEden")
        return None

class HHV(DetailView):
    template_name = 'polls/hhw.html'

    def get_object(self, **kwargs): # 352719086@qq.com
        # t = threading.Thread(name="hhv remind", target=sendhhv, args=(EMAIL_SUBJECT, MY_EMAIL_ADDR, ["352719086@qq.com", "707935952@qq.com"],))
        # t.start()
        return None


class ArticleDetailViewOld(DetailView):
    template_name = 'polls/article_detail_old.html'

    def get_object(self, **kwargs):
        articleId = self.kwargs.get('articleId')
        writeLoggerData(self.request, "ArticleDetailViewOld"+str(articleId))

        try:
            article = Article.objects.get(id=articleId)
            article.views += 1
            article.save()
            article.tags = article.tags.split()
            # print article.created
            article.created = str(article.created).split(' ')[0]
            date_list = article.created.split('-')
            article.cr_mon = date_list[1]
            if article.cr_mon[0] == '0':
                article.cr_mon = article.cr_mon[1]
            article.cr_day = date_list[2]
            if article.cr_day[0] == '0':
                article.cr_day = article.cr_day[1]

        except Article.DoesNotExist:
            raise Http404("Article does not exist")
        return article

class ArticleEditView(FormView):
    template_name = 'polls/article_publish.html'
    form_class = ArticlePublishForm
    article = None
    articleId = -1

    def get_initial(self, **kwargs):
        self.articleId = self.kwargs.get('articleId')
        try:
            self.article = Article.objects.get(id=self.articleId)
            initial = {
                'title': self.article.title,
                'content': self.article.content_html,
                'tags': self.article.tags,
            }
            return initial
        except Article.DoesNotExist:
            raise Http404("Article does not exist")

    def form_valid(self, form):
        userId = self.request.session['userId']
        userName = Userinfo.objects.get(id=userId).username
        form.save(userName, self.article)
        return super(ArticleEditView, self).form_valid(form)

    def get_success_url(self):
        # success_url = reverse('polls:article_detail', args=(self.articleId, 1))
        success_url = reverse('polls:article_edit', args=(self.articleId))
        return success_url

class RegisterView(FormView):
    template_name = 'polls/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('polls:blog_index')

    def form_valid(self, form):
        writeLoggerData(self.request, "Register")
        form.save()
        email = form.cleaned_data.get('email')
        rand_github_id = random.randint(1, 28)
        rand_github_avatar = "github" + str(rand_github_id) + ".png"

        userInfo = Userinfo.objects.get(email=email)
        userInfo.avatar_url = rand_github_avatar
        userInfo.save()

        self.request.session['userId'] = userInfo.id
        self.request.session['avatar'] = "/static/polls/userAvatar/" + rand_github_avatar
        # password = form.cleaned_data.get('password')

        return super(RegisterView, self).form_valid(form)


class TestView(DetailView):
    template_name = 'polls/test_fire.html'

    def get_object(self, **kwargs):
        return None

class NoneView(DetailView):
    template_name = 'polls/none.html'

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "NoneView")
        return None

class LogView(DetailView):
    template_name = "polls/log.html"

    def get_object(self, **kwargs):
        return None

class HelloWorldView(DetailView):
    template_name = "polls/hw.html"

    def get_object(self, **kwargs):
        writeLoggerData(self.request, "HelloWorldView")
        return None

class LoginView(FormView):
    # template_name = 'polls/login.html'
    template_name = 'polls/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('polls:blog_index')

    def form_valid(self, form):
        writeLoggerData(self.request, "Login")
        # email = self.request.POST.get('email')
        # messages.success(self.request, 'hreljh')
        email = form.cleaned_data.get('email')
        # password = form.cleaned_data.get('password')
        userInfo = Userinfo.objects.get(email=email)
        userId = userInfo.id
        userAvatar = userInfo.avatar_url
        self.request.session['userId'] = userId
        self.request.session['avatar'] = "/static/polls/userAvatar/" + userAvatar

        return super(LoginView, self).form_valid(form)

def Logout(request):
    writeLoggerData(request, "Logout")
    try:
        del request.session['userId']
        del request.session['avatar']
    except KeyError:
        pass

    # messages.success(request, "logout!")
    return HttpResponseRedirect(reverse('polls:blog_index'))

def sendhhv(s_emailsubject, s_emailaddr, s_emailaddrs):
    while True:
        time.sleep(10)
        now = int(time.time()) % 86400
        if now >= 57900  and now <= 57930:
            try:
                send_mail(s_emailsubject, u'来自可弟的提示信息：请及时填写健康码哦~', s_emailaddr, s_emailaddrs, fail_silently=False)
            except Exception as e:
                print(e)
                print('resend...')
                try:
                    send_mail(s_emailsubject, u'来自可弟的提示信息：请及时填写健康码哦~', s_emailaddr, s_emailaddrs, fail_silently=False)
                except:
                    print('sent email error!')

# 邮件发送
def sendEmailLike(s_emailsubject, s_emailaddr, s_emailaddrs):
    try:
        send_mail(s_emailsubject, u'有人给你点了赞...', s_emailaddr, s_emailaddrs, fail_silently=False)
    except Exception as e:
        print(e)
        print('resend...')
        try:
            send_mail(s_emailsubject, u'有人给你点了赞...', s_emailaddr, s_emailaddrs, fail_silently=False)
        except:
            print('sent email error!')


def LimeMeOp(request):

    likeOp = request.GET.get('op')
    if likeOp == "1":
        likeCount = 1
        # 数据统计
        writeLoggerData(request, "LimeMeOp")

        # 邮件发送
        # sendEmailLike(EMAIL_SUBJECT, MY_EMAIL_ADDR, [MY_EMAIL_ADDR])
        t = threading.Thread(name="LikeThread", target=sendEmailLike, args=(EMAIL_SUBJECT, MY_EMAIL_ADDR, [MY_EMAIL_ADDR],))
        t.start()
    elif likeOp == "2":
        likeCount = 0
    object_likeme = LikeMeData.objects.get(id=1)
    object_likeme.LikeMeCount += likeCount
    object_likeme.save()
    ret_json = {'r': object_likeme.LikeMeCount}
    return JsonResponse(ret_json)

def SendDM(request):
    dmValue = request.GET.get('dmValue')
    writeLoggerData(request, "SendDM: " + str(dmValue))
    try:
        avatar = request.session['avatar']
    except KeyError:
        avatar = "/static/polls/userEmotion/cute_shortcut.jpg"

    # print(avatar)
    consumers.ws_sendDM(avatar, dmValue)
    ret_json = {'r': 1}
    return JsonResponse(ret_json)

def MsgLike(request):
    # -1--评论 1 2 3--回复
    # 使用get没问题的

    # 后面有需要再加上邮件通知
    commentId = int(request.GET.get('commentId'))
    replyId = int(request.GET.get('replyId'))
    writeLoggerData(request, "MsgLike: " + str(commentId) + '-' + str(replyId))
    userId = request.session['userId']
    msg = SingleMsgBoard.objects.get(id=commentId)
    msg_list = pickle.loads(msg.msg_pickle_str)
    if (replyId == -1):
        replyId = 0

    # 处理数据
    like_set = msg_list[replyId][4]
    if userId in like_set:
        like_set.remove(userId)
        ret_json = {'likedNum':len(like_set), 'isLiked': 0}
    else:
        like_set.add(userId)
        ret_json = {'likedNum':len(like_set), 'isLiked': 1}
    msg.msg_pickle_str = pickle.dumps(msg_list)
    msg.save()

    return JsonResponse(ret_json)

# 删除某条评论及所有子回复  或者  删除某条子回复
def DeleteMsg(request):
    msgId = int(request.GET.get('msgId'))
    replyId = int(request.GET.get('replyId'))
    writeLoggerData(request, "DeleteMsg: " + str(msgId) + '-' + str(replyId))
    msg = SingleMsgBoard.objects.get(id=msgId)
    reply_list = pickle.loads(msg.msg_pickle_str)
    reply_list[replyId][1] = 0
    if replyId == 0:
        msg.is_exist = 0
    msg.msg_pickle_str = pickle.dumps(reply_list)
    msg.save()

    ret_json = {'retVal': 0}
    return JsonResponse(ret_json)

def generateRandomString10():
    sRet = ""
    for _ in range(10):
        sRet += random.choice('0123456789abcdefghijklmnopqrstuvwxyz')

    return sRet

def getArticleTitleByArticleId(ArticleId):
    if int(ArticleId) == 1001:
        return u"轻语"
    if int(ArticleId) == 1002:
        return u"充电"
    ArticleObject = Article.objects.get(id=ArticleId)
    return ArticleObject.title


def getArticleUrlByArticleId(ArticleId):
    if int(ArticleId) == 1001:
        return reverse('polls:msgboard', kwargs={"page":1, "articleId":1001})
    if int(ArticleId) == 1002:
        return reverse('polls:donate', kwargs={"page":1})
    return reverse('polls:article_detail', kwargs={"page":1, "articleId":int(ArticleId)})

def getEmailByUserName(userName):
    if not userName:
        return MY_EMAIL_ADDR
    return Userinfo.objects.get(username=userName).email

def getMsgEmailBodyByArticleId(ArticleId):
    sTitle = getArticleTitleByArticleId(ArticleId)
    sUrl = getArticleUrlByArticleId(ArticleId)
    sBody = u"某个小可爱在[" + sTitle + u"]中回复了你，还不去看看呀poi~(http://nasaco.club" + sUrl + u")"

    return sBody

# 邮件发送
def sendEmailReply(s_emailsubject, s_emailbody, s_myaddr, s_emailnamelist):
    try:
        send_mail(s_emailsubject, s_emailbody, s_myaddr, s_emailnamelist, fail_silently=False)
    except:
        print('resend...')
        try:
            send_mail(s_emailsubject, s_emailbody, s_myaddr, s_emailnamelist, fail_silently=False)
        except:
            print('sent email error!')

def AddOrReplyMsg(request):
    # page = int(request.GET.get(page))
    articleId = int(request.GET.get('articleId'))
    commentId = int(request.GET.get('commentId'))
    replyToName = request.GET.get('replyToName')

    # 邮件发送
    # sendEmailReply(EMAIL_SUBJECT, getMsgEmailBodyByArticleId(articleId), MY_EMAIL_ADDR, [getEmailByUserName(replyToName)])
    t = threading.Thread(name="ReplyThread", target=sendEmailReply, args=(EMAIL_SUBJECT, getMsgEmailBodyByArticleId(articleId), MY_EMAIL_ADDR, [getEmailByUserName(replyToName)],))
    t.start()

    # try:
    #     send_mail(EMAIL_SUBJECT, getMsgEmailBodyByArticleId(articleId), MY_EMAIL_ADDR, [getEmailByUserName(replyToName)], fail_silently=False)
    # except:
    #     print('resend...')
    #     try:
    #         send_mail(EMAIL_SUBJECT, getMsgEmailBodyByArticleId(articleId), MY_EMAIL_ADDR, [getEmailByUserName(replyToName)], fail_silently=False)
    #     except:
    #         print('sent email error!')

    content = request.GET.get('content')
    writeLoggerData(request, "AddOrReplyMsg: " + str(articleId) + \
                    "-" + str(commentId) + "-" + str(replyToName) + \
                    "-" + str(content))

    try:
        userId = request.session['userId']
        # 为了测试python3注释掉print
        # print userId
    except KeyError:
        userId = -1
        return

    timeNow = str(datetime.datetime.now())

    if commentId == -1:
        msg_list = [[userId, 1, timeNow, content, set(), replyToName]]
        sMsgList = pickle.dumps(msg_list)
        sHashString = generateRandomString10()

        single_msg_board = SingleMsgBoard(
            article_id = articleId,
            msg_pickle_str = sMsgList,
            is_exist = 1,
            hash_value = sHashString
        )
        single_msg_board.save()
        # use hash_value to get CommentId
        iCId = SingleMsgBoard.objects.get(hash_value=sHashString).id
        iRId = 0

    else:
        reply_item = [userId, 1, timeNow, content, set(), replyToName]
        comment_msg = SingleMsgBoard.objects.get(id=commentId)
        list_item = pickle.loads(comment_msg.msg_pickle_str)
        # print list_item
        list_item.append(reply_item)
        # print list_item
        sMsgList = pickle.dumps(list_item)
        comment_msg.msg_pickle_str = sMsgList
        comment_msg.save()
        iCId = commentId
        iRId = len(list_item) - 1

    # return dict
    # 包含基本的list 和 commentId && replyId
    userInfo = Userinfo.objects.get(id=userId)
    infoList = [userInfo.username, userInfo.sex, int(userInfo.com_power/COM_POWER_RATE), userInfo.level_tag, \
                userInfo.avatar_url]
    ret_json = {'userId': userId, 'date': timeNow.split('.')[0], \
                'username': infoList[0], 'sex': infoList[1], 'power': infoList[2], \
                'level_tag': infoList[3], 'avatar_url': infoList[4], 'commentId': iCId, \
                'replyId': iRId}

    return JsonResponse(ret_json)


def newAvatar(request):
    context = {}
    return render(request, "polls/avatar.html", context)

def UploadImg(request):
    context = {}
    return render(request, "polls/upimg.html", context)

@csrf_exempt
def UploadUserImage(request):
    if request.method == 'POST':
        base64_img = request.POST.get('image').split(',', 1)[1]
        img = base64.b64decode(base64_img)
        try:
            userId = str(request.session['userId'])
        except KeyError:
            userId = "noUser"
        # local
        # avatar_path_head = "/root/Nekko0/Nekko0/polls/static/polls/userAvatar/"
        # remote
        avatar_path_head = "/root/Nekko0/nekko0/Nekko0/polls/static/polls/userAvatar/"
        avatar_path = avatar_path_head + userId + ".png"
        with open(avatar_path, 'wb+') as dst:
            dst.write(img)

        set_ava_user = Userinfo.objects.get(id=userId)
        set_ava_user.avatar_url = userId + ".png"
        set_ava_user.save()
        request.session['avatar'] = "/static/polls/userAvatar/" + userId + ".png"
        ret_json = {'result': '图像已提交到数据中心！'}
        return JsonResponse(ret_json)

@csrf_exempt
def UploadImageCanon(request):
    if request.method == 'POST':
        base64_img = request.POST.get('image').split(',', 1)[1]
        img = base64.b64decode(base64_img)
        # avatar_path_head = "/root/Nekko0/nekko0/Nekko0/polls/static/polls/ImageCanon/"
        avatar_path_head = "/root/nekko/Nekko0/Nekko0/polls/static/polls/ImageCanon/"
        curTime = datetime.datetime.now()
        image_path = avatar_path_head + str(curTime.year) + "_" + str(curTime.month) + "_" + str(curTime.day) + "_" \
                     + str(curTime.hour) + "_" + str(curTime.minute) + "_" + str(curTime.second) + ".jpeg"
        with open(image_path, 'wb+') as dst:
            dst.write(img)

        ret_json = {'result': image_path}
        return JsonResponse(ret_json)

@csrf_exempt
def UploadImageCanonOSAKA(request):
    if request.method == 'POST':
        base64_img = request.POST.get('image').split(',', 1)[1]
        img = base64.b64decode(base64_img)
        # avatar_path_head = "/root/Nekko0/nekko0/Nekko0/polls/static/polls/ImageCanonOSAKA/"
        avatar_path_head = "/root/nekko/Nekko0/Nekko0/polls/static/polls/ImageCanonOSAKA/"
        curTime = datetime.datetime.now()
        image_path = avatar_path_head + str(curTime.year) + "_" + str(curTime.month) + "_" + str(curTime.day) + "_" \
                     + str(curTime.hour) + "_" + str(curTime.minute) + "_" + str(curTime.second) + ".jpeg"
        with open(image_path, 'wb+') as dst:
            dst.write(img)

        ret_json = {'result': image_path}
        return JsonResponse(ret_json)

def UploadAvatar(request):
    # print request.POST.get('x')
    # print request.POST.get('y')
    # print request.POST.get('w')
    # print request.POST.get('h')
    # print request.POST.get('scale-w')
    # print request.POST.get('scale-h')
    return HttpResponseRedirect(reverse('polls:msgboard', kwargs={"page":1, "articleId":1001}))

class MsgBoardListView(ListView, FormView):
    template_name = 'polls/msgboard.html'
    form_class = MsgBoardForm
    success_url = reverse_lazy('polls:msgboard',\
                               kwargs={"page":1, "articleId":1001})
    articleId = -1
    # 如果是留言板，id必须传1001过来

    def get_queryset(self, **kwargs):
        page = self.kwargs.get('page')
        self.articleId = self.kwargs.get('articleId')
        writeLoggerData(self.request, "MsgBoardList: " + str(page) + \
                        "-" + str(self.articleId))
        object_list = SingleMsgBoard.objects.filter(article_id=self.articleId, is_exist=1).order_by(F('id').desc())
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        ret_object_list = []
        # message: cur Page && all page num
        # print paginator.num_pages
        # print page
        messages.info(self.request, str(paginator.num_pages) + '_' + str(page) + \
                      '_' + str(self.articleId))

        try:
            userId = self.request.session['userId']
        except KeyError:
            userId = None

        for pickled_msg in object_list:
            # 这是一整条评论
            pickle_reply_list = pickle.loads(pickled_msg.msg_pickle_str)
            # get userinfo by userid
            for pickle_reply_list_item in pickle_reply_list:
                # 处理点赞数据
                # 判断是否登录
                like_set = pickle_reply_list_item[4]
                likedNum = len(like_set)

                if userId and userId in like_set:
                    isLiked = 1
                else:
                    isLiked = 0
                pickle_reply_list_item[4] = [likedNum, isLiked]

                userid = pickle_reply_list_item[0]
                pickle_reply_list_item[2] = pickle_reply_list_item[2].split('.')[0]
                userInfo = Userinfo.objects.get(id=userid)
                # 加入username, sex, level, level_tag, avatar_url
                # com_power是算力值，需要换算成level
                append_list = [userInfo.username, userInfo.sex, int(userInfo.com_power/COM_POWER_RATE), \
                               userInfo.level_tag, userInfo.avatar_url]
                # append_list = [userInfo.username, userInfo.sex, userInfo.com_power, \
                #                userInfo.level_tag, userInfo.avatar_url]
                pickle_reply_list_item += append_list
                # 判断子评论的所属者是否是当前用户
                if userId and userId == userid:
                    isCurrentUser = 1
                    # isCurrentUser = 0
                else:
                    isCurrentUser = 0
                pickle_reply_list_item.append(isCurrentUser)

            ret_object_list.append([pickled_msg.id, pickled_msg.article_id, pickle_reply_list[0], pickle_reply_list[1:]])
            # print pickle.loads(pickled_msg.msg_pickle_str)
        return ret_object_list

    def form_valid(self, form):
        commentId = int(self.request.POST.get('reply-form-commentid'))
        replyToName = self.request.POST.get('reply-form-replyto-name')
        articleId = int(self.request.POST.get('get-article-id'))
        pageId = int(self.request.POST.get('get-page'))
        try:
            userId = self.request.session['userId']
            # print userId
            self.success_url = reverse('polls:msgboard',\
                                       kwargs={"page":pageId, "articleId":articleId})
        except KeyError:
            userId = -1
            # modify success url
            self.success_url = reverse('polls:login')
        form.save(userId, articleId, commentId, replyToName)
        return FormView.form_valid(self, form)


class CodeDetailView(ListView, FormView):
    template_name = 'polls/code_detail.html'
    form_class = MsgBoardForm
    articleId = -1
    success_url = reverse_lazy('polls:code_detail',\
                               kwargs={"page":1, "articleId":articleId})
    # 如果是留言板，id必须传1001过来

    def getPrevNext(self, aId):
        try:
            ar_list = Article.objects.filter(is_exist=1, tags="code").order_by(F('id').desc())
            ar_len = len(ar_list)
            for idx in range(ar_len):
                if int(ar_list[idx].id) == int(aId):
                    idx_prev = idx-1
                    idx_next = idx+1
                    break
        except Article.DoesNotExist:
            raise Http404("Article does not exist")

        ret_list = []
        if idx_prev >= 0:
            ret_list.append([ar_list[idx_prev].title, ar_list[idx_prev].id])
        else:
            ret_list.append(None)

        if idx_next <= (ar_len-1):
            ret_list.append([ar_list[idx_next].title, ar_list[idx_next].id])
        else:
            ret_list.append(None)

        return ret_list


    def getArticle(self, aId):
        prevNextList = self.getPrevNext(aId)
        try:
            article = Article.objects.get(id=aId)
            article.views += 1
            article.save()
            # 查找内容部分
            ar_cnt = article.content_html.split(SHOW_CONTENT_SPLIT)
            if len(ar_cnt) == 2:
                article.content_html = ar_cnt[1]

            article.tags = article.tags.split()
            # print article.created
            article.created = str(article.created).split(' ')[0]
            date_list = article.created.split('-')
            article.cr_mon = date_list[1]
            if article.cr_mon[0] == '0':
                article.cr_mon = article.cr_mon[1]
            article.cr_day = date_list[2]
            if article.cr_day[0] == '0':
                article.cr_day = article.cr_day[1]

        except Article.DoesNotExist:
            raise Http404("Article does not exist")
        article.prevNextList = prevNextList
        return article

    def get_queryset(self, **kwargs):
        page = self.kwargs.get('page')
        self.articleId = self.kwargs.get('articleId')
        writeLoggerData(self.request, "CodeDetail: " + str(page) + \
                        "-" + str(self.articleId))
        self.success_url = reverse('polls:article_detail', kwargs={"page":1, "articleId":self.articleId})
        object_list = SingleMsgBoard.objects.filter(article_id=self.articleId, is_exist=1).order_by(F('id').desc())
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        ret_object_list = []
        # message: cur Page && all page num
        # print paginator.num_pages
        # print page
        messages.info(self.request, str(paginator.num_pages) + '_' + str(page) + \
                      '_' + str(self.articleId))

        for pickled_msg in object_list:
            # 这是一整条评论
            # msg_pickle_bytes = bytes(pickled_msg.msg_pickle_str, encoding="utf-8")
            # print("---------------------------")
            # print(msg_pickle_bytes)
            # print("---------------------------")
            # print(type(msg_pickle_bytes))
            # print("---------------------------")
            pickle_reply_list = pickle.loads(pickled_msg.msg_pickle_str)
            # get userinfo by userid
            for pickle_reply_list_item in pickle_reply_list:
                # 处理点赞数据
                # 判断是否登录
                like_set = pickle_reply_list_item[4]
                likedNum = len(like_set)
                try:
                    userId = self.request.session['userId']
                except KeyError:
                    userId = None

                if userId and userId in like_set:
                    isLiked = 1
                else:
                    isLiked = 0
                pickle_reply_list_item[4] = [likedNum, isLiked]

                userid = pickle_reply_list_item[0]
                pickle_reply_list_item[2] = pickle_reply_list_item[2].split('.')[0]
                userInfo = Userinfo.objects.get(id=userid)
                # 加入username, sex, level, level_tag, avatar_url
                # com_power是算力值，需要换算成level
                append_list = [userInfo.username, userInfo.sex, int(userInfo.com_power/COM_POWER_RATE), \
                               userInfo.level_tag, userInfo.avatar_url]
                pickle_reply_list_item += append_list
                # 判断子评论的所属者是否是当前用户
                if userId and userId == userid:
                    isCurrentUser = 1
                    # isCurrentUser = 0
                else:
                    isCurrentUser = 0
                pickle_reply_list_item.append(isCurrentUser)

            ret_object_list.append([pickled_msg.id, pickled_msg.article_id, pickle_reply_list[0], pickle_reply_list[1:]])
            # print pickle.loads(pickled_msg.msg_pickle_str)
        # [评论列表, 文章model]
        return [ret_object_list, self.getArticle(self.articleId)]

    # 似乎没用了
    def form_valid(self, form):
        commentId = int(self.request.POST.get('reply-form-commentid'))
        replyToName = self.request.POST.get('reply-form-replyto-name')
        articleId = int(self.request.POST.get('get-article-id'))
        pageId = int(self.request.POST.get('get-page'))
        try:
            userId = self.request.session['userId']
            # print userId
            self.success_url = reverse('polls:article_detail',\
                                       kwargs={"page":pageId, "articleId":articleId})
        except KeyError:
            userId = -1
            # modify success url
            self.success_url = reverse('polls:login')
        form.save(userId, articleId, commentId, replyToName)
        return FormView.form_valid(self, form)

class DonateView(ListView, FormView):
    template_name = 'polls/donate.html'
    form_class = MsgBoardForm
    articleId = 1002
    # 如果是留言板，id必须传1001过来
    # 充电id1002

    def get_queryset(self, **kwargs):
        page = self.kwargs.get('page')
        writeLoggerData(self.request, "DonateView" + str(page))
        self.articleId = 1002
        object_list = SingleMsgBoard.objects.filter(article_id=self.articleId, is_exist=1).order_by(F('id').desc())
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        ret_object_list = []
        # message: cur Page && all page num
        # print paginator.num_pages
        # print page
        messages.info(self.request, str(paginator.num_pages) + '_' + str(page) + \
                      '_' + str(self.articleId))

        for pickled_msg in object_list:
            # 这是一整条评论
            # msg_pickle_bytes = bytes(pickled_msg.msg_pickle_str, encoding="utf-8")
            # print("---------------------------")
            # print(msg_pickle_bytes)
            # print("---------------------------")
            # print(type(msg_pickle_bytes))
            # print("---------------------------")
            pickle_reply_list = pickle.loads(pickled_msg.msg_pickle_str)
            # get userinfo by userid
            for pickle_reply_list_item in pickle_reply_list:
                # 处理点赞数据
                # 判断是否登录
                like_set = pickle_reply_list_item[4]
                likedNum = len(like_set)
                try:
                    userId = self.request.session['userId']
                except KeyError:
                    userId = None

                if userId and userId in like_set:
                    isLiked = 1
                else:
                    isLiked = 0
                pickle_reply_list_item[4] = [likedNum, isLiked]

                userid = pickle_reply_list_item[0]
                pickle_reply_list_item[2] = pickle_reply_list_item[2].split('.')[0]
                userInfo = Userinfo.objects.get(id=userid)
                # 加入username, sex, level, level_tag, avatar_url
                # com_power是算力值，需要换算成level
                append_list = [userInfo.username, userInfo.sex, int(userInfo.com_power/COM_POWER_RATE), \
                               userInfo.level_tag, userInfo.avatar_url]
                pickle_reply_list_item += append_list
                # 判断子评论的所属者是否是当前用户
                if userId and userId == userid:
                    isCurrentUser = 1
                    # isCurrentUser = 0
                else:
                    isCurrentUser = 0
                pickle_reply_list_item.append(isCurrentUser)

            ret_object_list.append([pickled_msg.id, pickled_msg.article_id, pickle_reply_list[0], pickle_reply_list[1:]])
            # print pickle.loads(pickled_msg.msg_pickle_str)
        # [评论列表]
        return [ret_object_list]

# class CORSMiddleware(object):
#     # 尝试解决跨域问题
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         response["Access-Control-Allow-Origin"] = "*"
#
#         return response


class ArticleDetailView(ListView, FormView):
    template_name = 'polls/article_detail.html'
    form_class = MsgBoardForm
    articleId = -1
    success_url = reverse_lazy('polls:article_detail',\
                               kwargs={"page":1, "articleId":articleId})
    # 如果是留言板，id必须传1001过来


    def getPrevNext(self, aId):
        try:
            ar_list = Article.objects.filter(is_exist=1).order_by(F('id').desc())
            ar_len = len(ar_list)
            for idx in range(ar_len):
                if int(ar_list[idx].id) == int(aId):
                    idx_prev = idx-1
                    idx_next = idx+1
                    break
        except Article.DoesNotExist:
            raise Http404("Article does not exist")

        ret_list = []
        if idx_prev >= 0:
            ret_list.append([ar_list[idx_prev].title, ar_list[idx_prev].id])
        else:
            ret_list.append(None)

        if idx_next <= (ar_len-1):
            ret_list.append([ar_list[idx_next].title, ar_list[idx_next].id])
        else:
            ret_list.append(None)

        return ret_list


    def getArticle(self, aId):
        prevNextList = self.getPrevNext(aId)
        try:
            article = Article.objects.get(id=aId)
            article.views += 1
            article.save()
            # 查找内容部分
            ar_cnt = article.content_html.split(SHOW_CONTENT_SPLIT)
            if len(ar_cnt) == 2:
                article.content_html = ar_cnt[1]

            article.tags = article.tags.split()
            # print article.created
            article.created = str(article.created).split(' ')[0]
            date_list = article.created.split('-')
            article.cr_mon = date_list[1]
            if article.cr_mon[0] == '0':
                article.cr_mon = article.cr_mon[1]
            article.cr_day = date_list[2]
            if article.cr_day[0] == '0':
                article.cr_day = article.cr_day[1]

        except Article.DoesNotExist:
            raise Http404("Article does not exist")
        article.prevNextList = prevNextList
        return article

    def get_queryset(self, **kwargs):
        page = self.kwargs.get('page')
        self.articleId = self.kwargs.get('articleId')
        writeLoggerData(self.request, "ArticleDetailView" + str(page) + \
                        "-" + str(self.articleId))
        self.success_url = reverse('polls:article_detail', kwargs={"page":1, "articleId":self.articleId})
        object_list = SingleMsgBoard.objects.filter(article_id=self.articleId, is_exist=1).order_by(F('id').desc())
        paginator = Paginator(object_list, 10)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        ret_object_list = []
        # message: cur Page && all page num
        # print paginator.num_pages
        # print page
        messages.info(self.request, str(paginator.num_pages) + '_' + str(page) + \
                      '_' + str(self.articleId))

        for pickled_msg in object_list:
            # 这是一整条评论
            # msg_pickle_bytes = bytes(pickled_msg.msg_pickle_str, encoding="utf-8")
            # print("---------------------------")
            # print(msg_pickle_bytes)
            # print("---------------------------")
            # print(type(msg_pickle_bytes))
            # print("---------------------------")
            pickle_reply_list = pickle.loads(pickled_msg.msg_pickle_str)
            # get userinfo by userid
            for pickle_reply_list_item in pickle_reply_list:
                # 处理点赞数据
                # 判断是否登录
                like_set = pickle_reply_list_item[4]
                likedNum = len(like_set)
                try:
                    userId = self.request.session['userId']
                except KeyError:
                    userId = None

                if userId and userId in like_set:
                    isLiked = 1
                else:
                    isLiked = 0
                pickle_reply_list_item[4] = [likedNum, isLiked]

                userid = pickle_reply_list_item[0]
                pickle_reply_list_item[2] = pickle_reply_list_item[2].split('.')[0]
                userInfo = Userinfo.objects.get(id=userid)
                # 加入username, sex, level, level_tag, avatar_url
                # com_power是算力值，需要换算成level
                append_list = [userInfo.username, userInfo.sex, int(userInfo.com_power/COM_POWER_RATE), \
                               userInfo.level_tag, userInfo.avatar_url]
                pickle_reply_list_item += append_list
                # 判断子评论的所属者是否是当前用户
                if userId and userId == userid:
                    isCurrentUser = 1
                    # isCurrentUser = 0
                else:
                    isCurrentUser = 0
                pickle_reply_list_item.append(isCurrentUser)

            ret_object_list.append([pickled_msg.id, pickled_msg.article_id, pickle_reply_list[0], pickle_reply_list[1:]])
            # print pickle.loads(pickled_msg.msg_pickle_str)
        # [评论列表, 文章model]
        return [ret_object_list, self.getArticle(self.articleId)]

    # 似乎没用了
    def form_valid(self, form):
        commentId = int(self.request.POST.get('reply-form-commentid'))
        replyToName = self.request.POST.get('reply-form-replyto-name')
        articleId = int(self.request.POST.get('get-article-id'))
        pageId = int(self.request.POST.get('get-page'))
        try:
            userId = self.request.session['userId']
            # print userId
            self.success_url = reverse('polls:article_detail',\
                                       kwargs={"page":pageId, "articleId":articleId})
        except KeyError:
            userId = -1
            # modify success url
            self.success_url = reverse('polls:login')
        form.save(userId, articleId, commentId, replyToName)
        return FormView.form_valid(self, form)
