from bs4 import BeautifulSoup

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']

soup = BeautifulSoup(''.join(doc), "html.parser")
# print(soup.prettify())

tag_ps = soup.find_all("p", id="firstpara")
for p in tag_ps:
    print(p)
