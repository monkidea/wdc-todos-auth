from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Todo


@login_required
def index(request):
    todos = Todo.objects.filter(owner=request.user)
    status = request.GET.get('status', 'all')
    if status == 'active':
        todos = todos.filter(completed=False)
    elif status == 'completed':
        todos = todos.filter(completed=True)

    pending_count = todos.filter(completed=False).count()
    return render(request, 'ugly.html', {
        'todos': todos,
        'filter': status,
        'pending_count': pending_count
    })


@login_required
def create(request):
    Todo.objects.create(
        title=request.POST['title'],
        owner=request.user)
    return redirect('/')


@login_required
def toggle(request):
    todo = get_object_or_404(Todo, id=request.POST['todo_id'])
    if todo.owner != request.user:
        return HttpResponseForbidden('Not your todo')
    todo.completed = not todo.completed
    todo.save()
    return redirect('/')


@login_required
def destroy(request):
    todo = get_object_or_404(Todo, id=request.POST['todo_id'])
    if todo.owner != request.user:
        return HttpResponseForbidden('Not your todo')
    todo.delete()
    return redirect('/')
