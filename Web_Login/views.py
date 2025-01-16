from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView, DetailView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from Web_Login.models import Profile
from Web_Main.models import Item
from Web_Login.forms import ProfileForm, SignUpForm, ToolListForm

# Message
from django.contrib import messages

# Create your views here.

def sign_up(request):
    form=SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return HttpResponseRedirect(reverse('Web_Login:login'))
    return render(request, 'Web_Login/signup.html', context={'form':form})

def login_user(request):
    form= AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Web_Main:index'))
    return render(request, 'Web_Login/login.html', context={'form':form})

# class profile_view(DetailView):
#     model = Profile
#     userTools = Item.objects.all().filter(author = model.user)
#     template_name = "Web_Login/profile.html"
    
def profile_view(request, pk):
    profile = Profile.objects.get(id = pk)
    userTools = Item.objects.all().filter(author = profile.user)
    context={'profile':profile, 'userTools':userTools}
    return render(request, "Web_Login/profile.html", context)

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, 'You have been logged out!')
    return HttpResponseRedirect(reverse('Web_Main:index'))

@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            form = ProfileForm(instance=profile)
    return render(request, 'Web_Login/profile.html', context={'form':form})

@login_required
def listTool(request):
    form = ToolListForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = ToolListForm(request.POST, request.FILES)
        if form.is_valid():
            setTool = form.save(commit=False)
            setTool.author = request.user
            setTool.save
            messages.success(request, 'Tool listed successfully!')
            return HttpResponseRedirect(reverse('Web_Main:index'))
    return render(request, 'Web_Main/listTool.html', context={'form':form})

def item_view(request, pk):
    model = Item.objects.get(id = pk)
    allTools = Item.objects.all()
    userEmail = model.author
    userData = Profile.objects.get(user = userEmail)
    categoryTools = Item.objects.all().filter(category = model.category)[:3]

    images = [model.image_2, model.image_3, model.image_4, model.image_5]

    context={'model':model, 'allTools':allTools, 'userData':userData, 'images':images, 'categoryTools':categoryTools}
    return render(request, "Web_Main/item.html", context)

@login_required
def user_messages(request):
    return render(request, 'Web_Profile/messages.html')

@login_required
def edit_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated')
            return HttpResponseRedirect(reverse('Web_Main:index'))
    return render(request, 'Web_Profile/edit_profile.html', context={'form':form})