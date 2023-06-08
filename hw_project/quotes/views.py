from bson import ObjectId

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View

from .forms import AuthorForm, QuoteForm
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author_info(request, id):
    db = get_mongodb()
    author = db.authors.find_one({"_id": ObjectId(id)})
    return render(request, 'quotes/author_info.html', context={'author': author})


class AddAuthorView(View):
    form_class = AuthorForm
    template_name = "quotes/add_author.html"

    # def dispatch(self, request, *args, **kwargs):
    # if request.user.is_authenticated:
    # return redirect(to="quotes:root")
    # return super(AddAuthorView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"{username}, excellent! Author added successfully.")
            return redirect(to="quotes:root")

        return render(request, self.template_name, {"form": form})


class AddQuoteView(View):
    form_class = QuoteForm
    template_name = "quotes/add_quote.html"

    # def dispatch(self, request, *args, **kwargs):
    # if request.user.is_authenticated:
    # return redirect(to="quotes:root")
    # return super(AddQuoteView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"{username}, excellent! Quote added successfully.")
            return redirect(to="quotes:root")

        return render(request, self.template_name, {"form": form})
