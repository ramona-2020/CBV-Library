from django.urls import path

from library.book.old_views import index
from library.book.views import IndexView, AuthorListView, AuthorCreateView, AuthorDetailView, \
    SearchResultView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailByCodeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('author-list', AuthorListView.as_view(), name='author list page'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author details page'),
    path('author/create/', AuthorCreateView.as_view(), name='author create page'),

    path('book-list/', SearchResultView.as_view(), name='book list page'),
    path('book/create/', BookCreateView.as_view(), name='book create page'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book update page'),
    path('book/<int:code>/', BookDetailByCodeView.as_view(), name='book detail by code page'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book delete page'),
]



