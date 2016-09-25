from django.shortcuts import render, redirect, render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

try:
    from django.utils import simplejson as json
except ImportError:
    import json


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    liked_posts = Post.objects.filter(likes=request.user.pk)
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'board/post_list.html', {'posts': posts, 'liked_posts': liked_posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'board/post_edit.html', {'form': form})

def contributor_posts(request, contributor):
    posts = Post.objects.filter(contributor=contributor).order_by('-published_date')
    return render(request, 'board/post_list.html', {'posts': posts})

def genre_posts(request, content_type):
    posts = Post.objects.filter(content_type=content_type).order_by('-published_date')
    return render(request, 'board/post_list.html', {'posts': posts})

def remember_posts(request, when):
    posts = Post.objects.filter(when=when).order_by('-published_date')
    return render(request, 'board/post_list.html', {'posts': posts})

def user_posts(request, author):
    posts = Post.objects.filter(author__username=author).order_by('-published_date')
    return render(request, 'board/post_list.html', {'posts': posts})

def to_posts(request, to_field):
    posts = Post.objects.filter(to_field=to_field).order_by('-published_date')
    return render(request, 'board/post_list.html', {'posts': posts})

def my_list(request):
    posts = Post.objects.filter(likes=request.user.pk).order_by('-published_date')
    return render(request, 'board/post_list.html', {'posts': posts})


#Parameters in the def are recieved from the url
#Second argument in return defines which template
#Third argument in return function defines what object will be available in the templates


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect('/')

    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('post_list.html')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'registration/login.html', {})


class CommentCreate(CreateView):
    model = Comment
    fields = ['entry']

    def get_success_url(self):
        return reverse("post_detail", kwargs = {"pk": self.kwargs["post"]})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["post"])
        return super(CommentCreate, self).form_valid(form)


@login_required(login_url='/user')
def like_button(request):
    if request.method == 'POST':
        user = request.user
        id = request.POST.get('pk', None)
        post = get_object_or_404(Post, pk=id)

        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
        else:
            post.likes.add(user)

    context = {'likes_count': post.total_likes}
    return JsonResponse(context)


@login_required(login_url='/user')
def daily_button(request):
    if request.method == 'POST':
        user = request.user
        id = request.POST.get('pk', None)
        post = get_object_or_404(Post, pk=id)
            
        if post.weekly_follows.filter(id=user.id).exists():
            post.weekly_follows.remove(user)
            post.daily_follows.add(user)
        if post.monthly_follows.filter(id=user.id).exists():
            post.monthly_follows.remove(user)
            post.daily_follows.add(user)
        if post.daily_follows.filter(id=user.id).exists():
            post.daily_follows.remove(user)
            post.all_follows.remove(user) 
        else:
            post.daily_follows.add(user)
            post.all_follows.add(user)

    context = {'daily_count': post.total_daily, 'weekly_count': post.total_weekly, 'monthly_count': post.total_monthly, 'all_count': post.total_all_follows_count}
    return JsonResponse(context)


@login_required(login_url='/user')
def weekly_button(request):
    if request.method == 'POST':
        user = request.user
        id = request.POST.get('pk', None)
        post = get_object_or_404(Post, pk=id)

        if post.daily_follows.filter(id=user.id).exists():
            post.daily_follows.remove(user)
            post.weekly_follows.add(user)
        if post.monthly_follows.filter(id=user.id).exists():
            post.monthly_follows.remove(user)
            post.weekly_follows.add(user)
        if post.weekly_follows.filter(id=user.id).exists():
            post.weekly_follows.remove(user)
            post.all_follows.remove(user) 
        else:
            post.weekly_follows.add(user)
            post.all_follows.add(user)

    context = {'daily_count': post.total_daily, 'weekly_count': post.total_weekly, 'monthly_count': post.total_monthly, 'all_count': post.total_all_follows_count}
    return JsonResponse(context)


@login_required(login_url='/user')
def monthly_button(request):
    if request.method == 'POST':
        user = request.user
        id = request.POST.get('pk', None)
        post = get_object_or_404(Post, pk=id)

        if post.daily_follows.filter(id=user.id).exists():
            post.daily_follows.remove(user)
            post.monthly_follows.add(user)
        if post.weekly_follows.filter(id=user.id).exists():
            post.weekly_follows.remove(user)
            post.monthly_follows.add(user)
        if post.monthly_follows.filter(id=user.id).exists():
            post.monthly_follows.remove(user)
            post.all_follows.remove(user) 
        else:
            post.monthly_follows.add(user)
            post.all_follows.add(user)

    context = {'daily_count': post.total_daily, 'weekly_count': post.total_weekly, 'monthly_count': post.total_monthly, 'all_count': post.total_all_follows_count}
    return JsonResponse(context)



def home(request):
    return render(request, 'board/home.html')



