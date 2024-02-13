from .models import Image
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout

def home(request):
    if request.user.is_authenticated:
        images=Image.objects.filter(user__username=request.user)
        return render(request, 'home.html',{'images':images})
    else:
        return redirect('auth_view')

def auth_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    registration_form = CustomUserCreationForm()
    login_form = AuthenticationForm()
    return render(request, 'auth.html', {'login_form': login_form, 'registration_form': registration_form})

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    return redirect('auth_view')

def register_view(request):
    if request.method == 'POST':
        registration_form = UserCreationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            messages.success(request, f"Account created successfully for {username}!")
            return redirect('auth_view')
        else:
            for field, errors in registration_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    return redirect('auth_view')


def image_upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        uploaded_files = []

        for uploaded_file in files:
            instance = Image(user=request.user, image=uploaded_file)
            instance.save()
            uploaded_files.append({
                'url': instance.image.url,
                'name': instance.image.name,
            })

        return redirect('home')
    else:
        return redirect('home')
    

def logout_view(request):
    logout(request)
    # Redirect to a desired page after logout
    return redirect('auth_view')