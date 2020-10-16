import requests
from bs4 import BeautifulSoup
import win10toast
import time


my_bool = True

page_to_search = requests.get("http://www.wojciechwydmuch.com/blog.php")
soup = BeautifulSoup(page_to_search.content, 'html.parser')
heading_h3 = soup.find_all("h3")


list_of_h3 = [k.text for k in heading_h3]


while my_bool:
    page_to_search = requests.get("http://www.wojciechwydmuch.com/blog.php")
    soup = BeautifulSoup(page_to_search.content, 'html.parser')
    heading_h3 = soup.find_all("h3")

    newer_list = [k.text for k in heading_h3]


    if newer_list != list_of_h3:
        toaster = win10toast.ToastNotifier()
        toaster.show_toast("New notification from NotifierApp", "Python caught changes on website", duration=10)
        heading_h3 = newer_list
    heading_h3 = newer_list
    time.sleep(10)





