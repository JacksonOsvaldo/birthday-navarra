from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import UserEvent


@login_required
def user_birthday(request):
    """
    Função que cria um novo aniversário
    """

    context = {}

    form = UserForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("accounts:home")
    context["form"] = form

    return render(request, "event/create_birthday.html", context)


@login_required
def update(request, id):
    """
    Função que atualiza os dados de um aniversário
    """

    user_event = UserEvent.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user_event)
    if form.is_valid():
        form.save()
        return redirect("accounts:home")
    return render(
        request, "event/update.html", {"form": form, "user_event": user_event}
    )


@login_required
def delete(request, id):
    """
    Função que remove um aniversário
    """

    employee = UserEvent.objects.get(id=id)
    employee.delete()
    return redirect("accounts:home")
