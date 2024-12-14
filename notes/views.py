from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def home(request):
    return render(request, 'index.html')

def note_list(request):
    notes = Note.objects.all()
    ctx = {'notes': notes}
    return render(request, 'notes/list.html', ctx)


def note_create(request):
    if request.method == 'POST':
        note_title = request.POST.get('note_title')
        content = request.POST.get('content')

        if note_title and content:
            Note.objects.create(
                note_title=note_title,
                content=content,
            )
        return redirect('notes:list')
    return render(request, 'notes/form.html')


def note_detail(request, notes_id):
    notes = get_object_or_404(Note, pk=notes_id)
    ctx = {'notes': notes}
    return render(request, 'notes/detail.html', ctx)


def note_delete(request, notes_id):
    notes = get_object_or_404(Note, pk=notes_id)
    notes.delete()
    return redirect('notes:list')


def note_update(request, notes_id):
    notes = get_object_or_404(Note, pk=notes_id)
    if request.method == 'POST':
        note_title = request.POST.get('note_title')
        content = request.POST.get('content')

        if note_title and content:
            notes.note_title = note_title
            notes.content = content
            notes.save()
            return redirect(notes.get_detail_url())
    ctx = {'notes': notes}
    return render(request, 'notes/form.html', ctx)

