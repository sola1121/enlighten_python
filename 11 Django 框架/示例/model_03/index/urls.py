from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"index/$", index_view),
    url(r"01_add/$", add_view),
    url(r"02_query/$", query_view),

    url(r"author_list/$", author_list),
    url(r"delete_author/(\d+)/$", delete_veiw, name="del_au"),
    url(r"update_author/(\d+)/$", update_view, name="up_au"),
    url(r"add_num/(\d+){2}/$", add_num_view, name='age_add_num'),
    url(r"query_something/$", query_Q_view),
    url(r"raw_query/$", raw_view),

    url(r"wife_author/$", wife_author_view),
    url(r"author_wife/$", author_wife_view),
    url(r"book_publisher/$", book_publisher_view),
    url(r"publisher_book/$", publisher_book_view),
    url(r"author_book/$", author_book_view),
    url(r"book_author/$", book_author_view),
    url(r"author_publisher/$", author_publisher_view),
    url(r"publisher_author/$", publisher_author_view),
    url(r"count_author/$", obj_count_view),

    url(r"lt_age/$", lt_age_view),
    url(r"contain_word/$", contain_word_view),
]
