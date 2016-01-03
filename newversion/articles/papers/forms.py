from django import forms

from .models import Book, Tag

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ["title", "tags", "issue_date", "note"]
        widgets = {"note": forms.widgets.Textarea()}

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["tag", "description"]

