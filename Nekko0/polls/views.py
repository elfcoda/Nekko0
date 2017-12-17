# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pickle
from PIL import Image

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from django.views.generic.list import ListView
from models import Article, SingleMsgBoard, Userinfo
# from django.urls import reverse
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from forms import ArticlePublishForm, RegisterForm, LoginForm, MsgBoardForm, UploadAvatarForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import base64
import random

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


class ArticleListView(ListView):
    template_name = 'polls/blog_index.html'

    def get_queryset(self, **kwargs):
        object_list = Article.objects.all().order_by(F('created').desc())
        paginator = Paginator(object_list, 10)
        page = self.request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        return object_list

class ArticlePublishView(FormView):
    template_name = 'polls/article_publish.html'
    form_class = ArticlePublishForm
    success_url = reverse_lazy('polls:blog_index')

    def form_valid(self, form):
        form.save(self.request.user.username)
        return super(ArticlePublishView, self).form_valid(form)

class ArticleDetailView(DetailView):
    template_name = 'polls/article_detail.html'

    def get_object(self, **kwargs):
        title = self.kwargs.get('title')
        try:
            article = Article.objects.get(title=title)
            article.views += 1
            article.save()
            article.tags = article.tags.split()
        except Article.DoesNotExist:
            raise Http404("Article does not exist")
        return article

class ArticleEditView(FormView):
    template_name = 'polls/article_publish.html'
    form_class = ArticlePublishForm
    article = None

    def get_initial(self, **kwargs):
        title = self.kwargs.get('title')
        try:
            self.article = Article.objects.get(title=title)
            initial = {
                'title': title,
                'content': self.article.content_md,
                'tags': self.article.tags,
            }
            return initial
        except Article.DoesNotExist:
            raise Http404("Article does not exist")



    def form_valid(self, form):
        form.save(self.request, self.article)
        return super(ArticleEditView, self).form_valid(form)

    def get_success_url(self):
        title = self.request.POST.get('title')
        success_url = reverse('polls:article_detail', args=(title,))
        return success_url

class RegisterView(FormView):
    template_name = 'polls/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('polls:blog_index')

    def form_valid(self, form):
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

class LoginView(FormView):
    # template_name = 'polls/login.html'
    template_name = 'polls/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('polls:blog_index')

    def form_valid(self, form):
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
    try:
        del request.session['userId']
        del request.session['avatar']
    except KeyError:
        pass

    # messages.success(request, "logout!")
    return render(request, "polls/blog_index.html")

def MsgLike(request):
    # -1--评论 1 2 3--回复
    # 使用get没问题的
    commentId = int(request.GET.get('commentId'))
    replyId = int(request.GET.get('replyId'))
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

@csrf_exempt
def UploadUserImage(request):
    if request.method == 'POST':
        base64_img = request.POST.get('image').split(',', 1)[1]
        img = base64.b64decode(base64_img)
        try:
            userId = str(request.session['userId'])
        except KeyError:
            userId = "noUser"
        avatar_path_head = "/root/Nekko0/Nekko0/polls/static/polls/userAvatar/"
        # avatar_path_head = "/root/Nekko0/Nekko0/Nekko0/polls/static/polls/userAvatar/"
        avatar_path = avatar_path_head + userId + ".png"
        with open(avatar_path, 'wb+') as dst:
            dst.write(img)

        set_ava_user = Userinfo.objects.get(id=userId)
        set_ava_user.avatar_url = userId + ".png"
        set_ava_user.save()
        request.session['avatar'] = "/static/polls/userAvatar/" + userId + ".png"
        ret_json = {'result': '图像已提交到数据中心！'}
        return JsonResponse(ret_json)

def UploadAvatar(request):
    print request.POST.get('x')
    print request.POST.get('y')
    print request.POST.get('w')
    print request.POST.get('h')
    print request.POST.get('scale-w')
    print request.POST.get('scale-h')
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
        object_list = SingleMsgBoard.objects.filter(article_id=self.articleId).order_by(F('id').desc())
        paginator = Paginator(object_list, 2)
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
            pickle_reply_list = pickle.loads(pickled_msg.msg_pickle_str)
            # get userinfo by userid
            for pickle_reply_list_item in pickle_reply_list:
                # 处理点赞数据
                # 判断是否登录
                like_set = pickle_reply_list_item[4]
                likedNum = len(like_set)
                userId = self.request.session['userId']
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
                append_list = [userInfo.username, userInfo.sex, userInfo.com_power, \
                               userInfo.level_tag, userInfo.avatar_url]
                pickle_reply_list_item += append_list

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
            print userId
            self.success_url = reverse('polls:msgboard',\
                                       kwargs={"page":pageId, "articleId":articleId})
        except KeyError:
            userId = -1
            # modify success url
            self.success_url = reverse('polls:login')
        form.save(userId, articleId, commentId, replyToName)
        return FormView.form_valid(self, form)


