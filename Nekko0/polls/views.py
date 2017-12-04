# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pickle

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
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
from forms import ArticlePublishForm, RegisterForm, LoginForm, MsgBoardForm
from django.contrib import messages

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
        userId = Userinfo.objects.get(email=email).id
        self.request.session['userId'] = userId
        # password = form.cleaned_data.get('password')

        return super(RegisterView, self).form_valid(form)

class LoginView(FormView):
    template_name = 'polls/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('polls:blog_index')

    def form_valid(self, form):
        # email = self.request.POST.get('email')
        # messages.success(self.request, 'hreljh')
        email = form.cleaned_data.get('email')
        # password = form.cleaned_data.get('password')
        userId = Userinfo.objects.get(email=email).id
        self.request.session['userId'] = userId

        return super(LoginView, self).form_valid(form)

def Logout(request):
    try:
        del request.session['userId']
    except KeyError:
        pass

    # messages.success(request, "logout!")
    return render(request, "polls/blog_index.html")

class MsgBoardListView(ListView, FormView):
    template_name = 'polls/msgboard.html'
    form_class = MsgBoardForm
    success_url = reverse_lazy('polls:msgboard', kwargs={"page":0})

    def get_queryset(self, **kwargs):
        object_list = SingleMsgBoard.objects.filter(article_id=1001).order_by(F('id').desc())
        paginator = Paginator(object_list, 10)
        page = self.request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        ret_object_list = []
        for pickled_msg in object_list:
            pickle_reply_list = pickle.loads(pickled_msg.msg_pickle_str)
            # get userinfo by userid
            for pickle_reply_list_item in pickle_reply_list:
                userid = pickle_reply_list_item[0]
                userInfo = Userinfo.objects.get(id=userid)
                # 加入username, sex, level, level_tag, avatar_url
                append_list = [userInfo.username, userInfo.sex, userInfo.level, \
                               userInfo.level_tag, userInfo.avatar_url]
                pickle_reply_list_item += append_list

            ret_object_list.append([pickled_msg.id, pickled_msg.article_id, pickle_reply_list[0], pickle_reply_list[1:]])
            # print pickle.loads(pickled_msg.msg_pickle_str)
        return ret_object_list

    def form_valid(self, form):
        commentId = int(self.request.POST.get('reply-form-commentid'))
        replyToName = self.request.POST.get('reply-form-replyto-name')
        articleId = 1001
        try:
            userId = self.request.session['userId']
        except KeyError:
            userId = -1
            # modify success url
        form.save(userId, articleId, commentId, replyToName)
        return FormView.form_valid(self, form)

class MsgBoardFormView(FormView):
    pass



