from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required #Para proteger una vista
from .forms import UserEditForm, ProfileEditForm
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Inicio de sesión exitoso.')
                    if not hasattr(user, 'profile'):  # Si no tiene perfil, lo creamos
                        Profile.objects.create(user=user)
                    return redirect('dashboard')  # Redirige al dashboard
                else:
                    messages.warning(request, 'Tu cuenta está inactiva.')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
     return render(request, 'account/dashboard.html')

@login_required
def edit_profile(request):
    # Verificar si el usuario tiene un perfil
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)  # Crear el perfil si no existe

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado exitosamente')
        else:
            messages.error(request, 'Hubo un error al actualizar el perfil')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 'account/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
