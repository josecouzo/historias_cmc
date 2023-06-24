from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, Group
# Create your views here.
from .forms import UserForm
from .models import UserData


def render_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios_index.html', {'usuarios': usuarios})


def create_user(request):
    data = None
    if request.method == 'POST':
        try:
            data = request.user.userdata
        except ObjectDoesNotExist:
            messages.error(request, "No puede usar este método, Si es superusuario emplee el panel",
                           extra_tags='alert-danger')
            return redirect(reverse('create_user'))
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email']).first()
            if user:
                messages.error(request, "Correo Electrónico en uso, por favor escoja uno diferente",
                               extra_tags='alert-danger')
                return redirect(reverse('create_user'))
            user = User.objects.filter(username=form.cleaned_data['username']).first()
            if user:
                messages.error(request, "Nombre de usuario en uso, por favor escoja uno diferente",
                               extra_tags='alert-danger')
                return redirect(reverse('create_user'))
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
            )
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            userdata = UserData(
                user=user,
                especialiad=form.cleaned_data['especialiad'],
                sexo=form.cleaned_data['sexo'],
                telefono=form.cleaned_data['telefono'],
            )
            userdata.save()
            messages.success(request, f"{user.username} agregado correctamente", extra_tags='alert-success')
            return redirect(reverse('users'))
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})


def create_user_super(request):
    User.objects.create_superuser('admin', 'jose.couzo95@example.com', 'Qwerty-1234')
    usuarios = User.objects.all()
    return render(request, 'usuarios_index.html', {'usuarios': usuarios})
