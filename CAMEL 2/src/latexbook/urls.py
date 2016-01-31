from django.conf.urls import url

from latexbook.views import BookNodeDetailView, BookNodeChapterDetailView, show_test

urlpatterns = [
    url(r"^(?P<pk>[0-9]+)/$", BookNodeDetailView.as_view(), name="latexbook_booknode_detail"),
    url(r"^(?P<book_pk>[0-9]+)/(?P<pk>[0-9]+)/$", BookNodeChapterDetailView.as_view(), name="latexbook_booknode_chapter_detail"),
    url(r"test/$", show_test, name="latexbook_test")
]