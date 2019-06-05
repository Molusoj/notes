from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NoteCreateForm
from django.views.generic.edit import CreateView
from .models import Note
from django.views.generic import ListView, DetailView
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


class HomePageView(ListView):
    template_name = 'notes/index.html'
    model = Note
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    template_name = 'notes/detail.html'
    model = Note
    context_object_name = 'note'

# def detail(request, note_id):
# 	note = get_object_or_404(Note, pk=note_id)
# 	return render(request, 'notes/detail.html', {'note':note})

class NoteCreateview(CreateView):
    model = Note
    template_name = 'notes/create.html'
    fields = ['title', 'body']
    success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('detail', instance.pk)
