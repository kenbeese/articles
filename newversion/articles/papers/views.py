from django.shortcuts import render
from django.views.decorators.http import require_POST

# Create your views here.
from .models import Book
from .forms import BookForm

def toppage(request):
    d={"book": Book.objects.all()}
    return render(request, "top.html", d)


def add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        Book.objects.create(**form.cleaned_data)
        return redirect(request, "papers:toppage")

    print(form)
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

