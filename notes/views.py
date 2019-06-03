from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NoteCreateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Note
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# @login_required
# def note_create(request):
#     if request.method == 'POST':
#         # form is sent
#         form = NoteCreateForm(data=request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             new_item = form.save(commit=False)
#             # Assign Current User to the item
#             new_item.user = request.user
#             new_item.save()
#             messages.success(request, 'Note Added')

#             # redirect to new created note detail view
#             return redirect(request, 'notes/create.html')
#         else:
#             return render(request, 'notes/create.html', {'error': 'All Fields Required'})
#     else:
#         return render(request, 'notes/create.html')


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'notes/index.html'
    model = Note
    context_object_name = 'notes'

    def get_queryset(self):
        notes = super().get_queryset()
        return notes.filter(user=self.request.user)

# def home(request):
#     notes = Note.objects
#     return render(request, 'notes/index.html', {'notes': notes})


class NoteDetailView(LoginRequiredMixin, DetailView):
    template_name = 'notes/detail.html'
    model = Note
    context_object_name = 'note'

    def get_queryset(self):
        notes = super().get_queryset()
        return notes.filter(user=self.request.user)


# def detail(request, note_id):
#   note = get_object_or_404(Note, pk=note_id)
#   return render(request, 'notes/detail.html', {'note':note})


class NoteCreateview(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/create.html'
    fields = ['title', 'body']

    def get_queryset(self):
        notes = super().get_queryset()
        return notes.filter(user=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('detail', instance.slug, instance.pk)

# @login_required
# def dashboard(request):
#     return render(request,
#                   'account/dashboard.html',
#                   {'section': 'dashboard'})


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'notes/update.html'
    fields = ['title', 'body']

    def get_queryset(self):
        notes = super().get_queryset()
        return notes.filter(user=self.request.user)

    def form_valid(self, form):
        instance = form.save()
        return redirect('detail', instance.slug, instance.pk)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/delete.html'
    success_url = '/'

    def get_queryset(self):
        notes = super().get_queryset()
        return notes.filter(user=self.request.user)
