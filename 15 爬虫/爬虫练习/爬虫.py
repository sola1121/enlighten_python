from urllib import request
from urllib import error

ua_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36"


def get_html(url, ua_agent=ua_agent, num_retries=5):
    head = {"User-Agent": ua_agent}
    req = request.Request(url, headers=head)
    try:
        res = request.urlopen(req)
        html_text = res.read().decode("utf-8")
        return html_text
    except error.HTTPError as err:
        print(err.code, err.reason)
        