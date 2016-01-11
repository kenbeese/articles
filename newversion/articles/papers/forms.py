from django import forms

from .models import Book, Tag, Author

class BookForm(forms.ModelForm):
    new_tags = forms.CharField(required=False)
    new_authors = forms.CharField(required=False)
    class Meta:
        model = Book
        fields = ["title", "tags", "new_tags", "authors", "new_authors", "bookfile"]
        widgets = {"note": forms.widgets.Textarea()}

    def save(self, commit=True):
        book = super(BookForm, self).save()# Save the book

        if not self.cleaned_data['new_tags'][0] == "":
            tags = [Tag.objects.create(tag=t) for t in self.cleaned_data['new_tags']]
            book.tags.add(*tags)

        if not self.cleaned_data['new_authors'][0] == "":
            authors = [Author.objects.create(name=a) for a in self.cleaned_data['new_authors']]
            book.tags.add(*authors)

        return book

    def clean_new_tags(self):
        data = self.cleaned_data['new_tags']
        data = [i.strip() for i in data.split(',')]
        return data

    def clean_new_authors(self):
        data = self.cleaned_data['new_authors']
        data = [i.strip() for i in data.split(';')]
        return data


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["tag", "description"]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]

