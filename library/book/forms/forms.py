import datetime

from django import forms

from library.book.helpers import BoostrapFormMixin
from library.book.models import Book


class BookCreateForm(BoostrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super()._init_bootstrap_fields()
        self.initial['genre'] = Book.ACTION

    class Meta:
        model = Book
        fields = '__all__'

        # The years are in the range [1920 ... this year]
        current_year = datetime.datetime.now().year

        widgets = {
            'author': forms.Select(),
            'title': forms.TextInput(),
            'pages': forms.NumberInput(),
            'code': forms.TextInput(),
            'slug': forms.TextInput(),
            'genre': forms.Select(),
            'date_published': forms.SelectDateWidget(
                years=range(1920, current_year + 1)
            )
        }


class BookUpdateForm(BoostrapFormMixin, forms.ModelForm):
    disabled_fields = 'genre'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super()._init_bootstrap_fields()
        super()._init_disabled_fields()


    class Meta:
        model = Book
        fields = '__all__'

        # The years are in the range [1920 ... this year]
        current_year = datetime.datetime.now().year

        widgets = {
            'author': forms.Select(),
            'title': forms.TextInput(),
            'pages': forms.NumberInput(),
            'code': forms.TextInput(),
            'slug': forms.TextInput(),
            'genre': forms.Select(),
            'date_published': forms.SelectDateWidget(
                years=range(1920, current_year + 1)
            )
        }

