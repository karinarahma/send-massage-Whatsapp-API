from selenium import webdriver
import urllib.parse as urlparse
from urllib.parse import urlencode

url = "https://api.whatsapp.com/send"
to_msg = {'phone' : '62859xxxxxxxx',
          'text' :  'Hello world'}

url_part = list(urlparse.urlparse(url))
query = dict(urlparse.parse_qsl(url_part[4]))
query.update(to_msg)
url_part[4] = urlencode(query)
link = urlparse.urlunparse(url_part)
driver = webdriver.Chrome()
driver.get(link)
#input('Enter anything after the window of whatsapp API')
driver.find_element_by_class_name('_whatsapp_www__block_action').click()
input('Enter anything to continue')
driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
input('Enter anything after scanning barcode')
driver.find_element_by_class_name('_1U1xa').click()
