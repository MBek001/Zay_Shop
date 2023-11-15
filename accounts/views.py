from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model,hashers,authenticate, login,logout
from django.contrib import messages
from .forms import LoginForm


User = get_user_model()


class RegisterView(View):
    template_name = 'regst.html'
    context = {}

    def get(self, request):
        return render(request, 'regst.html',self.context)

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')

        if password1 == password2:
            if User.objects.filter(username=username ).exists():
                messages.error(request, "This username already exists")
                return redirect('/accounts/register')
            if User.objects.filter(email = email).exists():
                messages.error(request, "This email already exsists")
                return redirect('/accounts/register')
            else:
                user = User.objects.create(
                    first_name=first_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    password = hashers.make_password(password2)
                )
                user.save()
                return redirect('/accounts/login')
        else:
            messages.error(request,"Passwords are not same !")
            return redirect('/accounts/register')


class LoginingView(View):
    template = "login.html"
    context = {}

    def get(self, request):
        form = LoginForm()
        self.context.update({'form': form})
        return render(request, self.template, self.context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Username or password is wrong !")

        return redirect('/accounts/login')

class LogoutingView(View):

    def get(self, request):
        logout(request)
        return redirect('/')
