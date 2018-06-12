from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from . import view, testdb, search, search2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
    url(r'^add_book$', view.add_book, ),
    url(r'^show_books$', view.show_books, ),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]