from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from event.models import UserEvent


@login_required
def index(request):
    """
    Função para listagem de todos os aniversário cadastrados
    """

    users = UserEvent.objects.all()
    return render(request, "index.html", {"users": users})


def sign_up(request):
    """
    Função para cadastro de novo usuário
    """

    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("accounts:home")
    context["form"] = form
    return render(request, "account/sign_up.html", context)


def logout_view(request):
    """
    Função para logout de usuário
    """

    logout(request)
    return redirect("accounts:home")
