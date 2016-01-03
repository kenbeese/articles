from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.
from .models import Book
from .forms import BookForm

def toppage(request):
    d={"books": Book.objects.all()}
    return render(request, "top.html", d)


def add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        Book.objects.create(**form.cleaned_data)
        return redirect("papers:top")
    d = {
    "form": form,
    }
    return render(request, "edit.html", d)


def edit(request, editing_id):
    book = get_object_or_404(Book, id=editing_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('papers:top')
    else:
        form = BookForm(instance=book)

    d = {
        "form": form,
    }
    return render(request, "edit.html", d)


@require_POST
def delete(request):
    # delete_ids = request.POST.getlist('delete_ids')
    # print delete_ids
    # if delete_ids:
    #     Book.objects.filter(id__in=delete_ids).delete()
    return redirect('paper:top')

