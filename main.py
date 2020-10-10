import requests
from bs4 import BeautifulSoup
from win10toast import *
import time

my_bool = True
my_list = []
page = requests.get("http://www.wojciechwydmuch.com/blog.php")
soup = BeautifulSoup(page.content, 'html.parser')
heading = soup.find_all("h3")

for k in heading:
    my_list.append(k.text)


while my_bool == True:
    newer = []
    page = requests.get("http://www.wojciechwydmuch.com/blog.php")
    soup = BeautifulSoup(page.content, 'html.parser')
    heading = soup.find_all("h3")

    for k in heading:
        newer.append(k.text)

    if newer != my_list:
        toaster = ToastNotifier()
        toaster.show_toast("New notification from NotifierApp", "Python caught changes on website", duration=10)
        my_list = newer
    my_list = newer
    time.sleep(10)





