from django.shortcuts import render, redirect
from typing import Any
from django.db.models.query import QuerySet
from django.db.models.base import Model as Model
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from friends.forms import SearchForm
from django.urls import reverse
from friendship.models import Friend, FriendshipRequest


@login_required
def friends_user(request: HttpRequest):
    return render(request, 'friends/friends.html')


class OtherUserProfile(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'User/profile.html'
    slug_url_kwarg = 'tag_user'
    context_object_name = 'post'
    
    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        user = get_object_or_404(self.model, tag_user=self.kwargs[self.slug_url_kwarg])
        return user


class SearchView(LoginRequiredMixin, FormView):
    form_class = SearchForm
    template_name = 'friends/search.html'
    
    
    def form_valid(self, form):
        self.form = form
        return redirect(self.get_success_url())
    
    
    def get_success_url(self):
        return reverse('friends:user-click', kwargs={'tag_user': self.form.cleaned_data['tag_search']})


@login_required
def add_friend(request: HttpRequest):
    user_tag = request.META['HTTP_REFERER'].split('/')[-1] # Получаем тег пользователя
    other_user = get_user_model().objects.get(tag_user=user_tag)
        
    Friend.objects.add_friend(
    request.user,
    other_user)
        
    FriendshipRequest.objects.get(from_user=request.user, to_user=other_user).accept()

    return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))


@login_required
def del_friend(request: HttpRequest):
    user_tag = request.META['HTTP_REFERER'].split('/')[-1] # Получаем тег пользователя
    other_user = get_user_model().objects.get(tag_user=user_tag)
        
    Friend.objects.remove_friend(request.user, other_user)

    return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))