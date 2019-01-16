import requests
import lxml.html as lh
import wget

home_url = 'https://cslu.ohsu.edu/~bedricks/courses/cs662/hw/HW1/GW-cna_eng/'
page  = requests.get(home_url)
html_doc = lh.fromstring(page.content)

tds = html_doc.xpath('//td/a/text()')
tds.remove('Parent Directory')
for td in tds:
    print(home_url + td)
    wget.download(home_url + td)


