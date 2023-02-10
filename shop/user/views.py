from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from django.urls import reverse
from django.views import generic

from .forms import UserCreateForm


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'user_detail.html'


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = UserCreateForm()
    return render(request, 'user_create.html', {'form': form})


class UserUpdateView(generic.UpdateView):
    model = User
    template_name = 'user_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('user:profile', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user.is_authenticated and user.id == request.user.id:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/')