from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r"01_request/$", request_view),

    url(r"02_login/$", login_view),
    url(r"^03_login_get/", get_view),
    url(r"^04_query/", query_view),

    url(r"05_form/$", form_view),
    url(r"06_register/$", register_form_view),

    url(r"07_model_form/$", model_form_view),

    url(r"08_add_cookie/$", add_cookie_view),
    url(r"09_get_cookie/$", get_cookie_view),
    url(r"10_set_session/$", set_session_view),
    url(r"11_get_session/$", get_session_view),
]