from django.db.models import Q

from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from library.book.forms.forms import BookCreateForm, BookUpdateForm
from library.book.models import Author, Book


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class Custom404View(TemplateView):
    template_name = '404.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'
    template_name = 'author-create.html'
    success_url = reverse_lazy('author list page')


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author-detail.html'


class BookListView(ListView):
    model = Book
    template_name = 'book-list.html'

    # def get_queryset(self):
    #     queryset = Book.objects.filter(
    #         Q(title__icontains='moa') | Q(title__icontains='lon')
    #     )
    #     return queryset


class BookCreateView(CreateView):
    model = Book
    template_name = 'book-create.html'
    success_url = reverse_lazy('book list page')
    form_class = BookCreateForm


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book-edit.html'
    form_class = BookUpdateForm
    success_url = reverse_lazy('book list page')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book-delete.html'
    success_url = reverse_lazy('book list page')


class BookDetailBySlugView(DetailView):
    model = Book
    template_name = 'book-detail.html'


class BookDetailByCodeView(DetailView):
    model = Book
    template_name = 'book-detail.html'

    def get_object(self, queryset=None):
        if self.kwargs.get('code', False):
            code = self.kwargs.get('code')
            try:
                book_ovbject = Book.objects.get(code=code)
                return book_ovbject
            except Book.DoesNotExist:
                raise Http404


class SearchResultView(ListView):
    model = Book
    template_name = 'book-list.html'

    def get_queryset(self):
        q = self.request.GET.get('q')

        queryset = Book.objects.all()
        if q:
            queryset = Book.objects.filter(
                Q(title__icontains=q)
            )

        return queryset
