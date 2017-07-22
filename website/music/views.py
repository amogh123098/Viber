import operator
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Album
from .models import Song
from django.views.generic import View
from .forms import UserForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):

    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    ordering = ['album_title']

    def get_queryset(self):

        return Album.objects.filter(owner=self.request.user)


@method_decorator(login_required, name='dispatch')
class SongListView(generic.ListView):

    template_name = 'music/song_list.html'
    context_object_name = 'songs'
    ordering = ['title']

    def get_queryset(self):

        return Song.objects.filter(album__owner=self.request.user)



@method_decorator(login_required, name='dispatch')
class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

    def get_queryset(self):

        return Album.objects.filter(owner=self.request.user)


@method_decorator(login_required, name='dispatch')
class SearchView(generic.ListView):
    template_name = 'music/song_list.html'
    context_object_name = 'songs'
    ordering = ['title']

    def get_queryset(self):
        if self.request.GET.get('q'):
            que = self.request.GET['q']
            print(que)
        else:
            return Song.objects.filter(album__owner=self.request.user)
        return Song.objects.filter(album__owner=self.request.user, song_title__startswith=que)


@method_decorator(login_required, name='dispatch')
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        self.object = obj
        obj.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    template_name_suffix = '_update_form'


@method_decorator(login_required, name='dispatch')
class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


@method_decorator(login_required, name='dispatch')
class SongCreate(CreateView):
    model = Song
    fields = ['song_title', 'file']

    def form_valid(self, form):
        obj = form.save(commit=False)
        new2 = self.kwargs['pk']
        obj.album = Album.objects.get(id=new2)
        self.object = obj
        obj.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class SongUpdate(UpdateView):
    model = Song
    fields = ['song_title', 'file']
    template_name_suffix = '_update_form'


@method_decorator(login_required, name='dispatch')
class SongDelete(DeleteView):
    model = Song

    def get_queryset(self):

        return Song.objects.filter(album__owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        new2 = self.object.album.pk
        self.object.delete()
        return HttpResponseRedirect(reverse('music:detail', kwargs={'pk': new2}))


@method_decorator(login_required, name='dispatch')
class AlbumFavorite(View):

    def dispatch(self, request, *args, **kwargs):
        album = Album.objects.get(pk=self.kwargs['pk'])
        if album.is_favorite:
            album.is_favorite = False
        else:
            album.is_favorite = True
        album.save()

        return redirect('music:index')


@method_decorator(login_required, name='dispatch')
class SongPlayer(generic.DetailView):
    model = Song
    template_name = 'music/music_player.html'

    def get_queryset(self):

        return Song.objects.filter(album__owner=self.request.user)


@method_decorator(login_required, name='dispatch')
class SongFavorite(View):

    def dispatch(self, request, *args, **kwargs):
        song = Song.objects.get(pk=self.kwargs['pk'])
        new2 = song.album.pk
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()

        return HttpResponseRedirect(reverse('music:detail', kwargs={'pk': new2}))


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # clean (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return user objects if credentials are correct

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})
