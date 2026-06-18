from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from dashboard.models import UserVerification, User


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        password = request.POST.get(
            'password'
        )

        login_type = request.POST.get(
            'login_type'
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            if (
                login_type == 'admin'
                and not user.is_superuser
            ):

                messages.error(
                    request,
                    'Not an admin account.'
                )

                return render(
                    request,
                    'accounts/login.html'
                )

            login(request, user)

            if user.is_superuser:
                return redirect(
                    'admin_dashboard'
                )

            return redirect(
                'user_dashboard'
            )

        messages.error(
            request,
            'Invalid username or password.'
        )

    return render(
        request,
        'accounts/login.html'
    )


def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            try:
                verification = ( UserVerification.objects.get(employee_id=employee_id))

            except UserVerification.DoesNotExist:
                form.add_error('employee_id','User ID is not authorised.' )
                return render( request,'accounts/register.html',{'form': form})

            if verification.is_registered:
                form.add_error('employee_id', 'This User ID is already registered.')
                return render(request, 'accounts/register.html',{'form': form})

            if User.objects.filter( username=username).exists():
                form.add_error('username', 'Username already exists.')
                return render( request,'accounts/register.html',{'form': form})

            user = User.objects.create_user(
                username=username,
                password=password
            )

            verification.user = user
            verification.is_registered = True
            verification.save()

            messages.success(request,'Registration successful.')
            return redirect('login')

    return render(
        request,'accounts/register.html',{'form': form}
    )


def logout_view(request):
    logout(request)
    return redirect('login')