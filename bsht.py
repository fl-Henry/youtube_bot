import itertools
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from seleniumwire import webdriver as wire_webdriver


class ProxyRotator:
    def __init__(self, proxies):
        # create iterator, which will cycle through the proxies
        self.proxies = itertools.cycle(proxies)
        self.current_proxy = None
        self.good_proxy = {}
        # counter of request to change proxy
        self.request_counter = 0

    def change_proxy(self):
        # Change the proxy to the next one and reset the counter
        self.current_proxy = next(self.proxies)
        self.request_counter = 0
        return self.current_proxy

    def get_proxy(self):
        # check if the proxy has to be changed ("2" means change after every second request)
        if self.request_counter % 2 == 0:
            self.change_proxy()
        self.request_counter += 1
        return self.current_proxy

proxies = [
    {
        'http': "socks5://3QLrMH:efE58u@194.67.201.65:9282",
        'https': "socks5://3QLrMH:efE58u@194.67.201.65:9282"
    },
    {
        'http': "socks5://Y8XABo:JWeAHQ@194.67.223.202:9365", 'https':
        "socks5://Y8XABo:JWeAHQ@194.67.223.202:9365"
    },
    {
        'http': "socks5://4bL6Jn:SEKwVS@196.18.167.105:8000", 'https':
        "socks5://4bL6Jn:SEKwVS@196.18.167.105:8000"
    },
    {
        'http': "socks5://wRKZPG:snFyfD@91.229.113.96:8000",
        'https':"socks5://wRKZPG:snFyfD@91.229.113.96:8000"
    }
]

proxy_rotator = ProxyRotator(proxies)

while True:
    proxy = proxy_rotator.get_proxy()
    print(f'using proxy: {proxy}')
    prx = {}
    prx.update({'proxy': proxy})
    with wire_webdriver.Chrome(seleniumwire_options=prx) as browser:
        browser.get("http://httpbin.org/ip")
        print(browser.find_element(By.TAG_NAME, 'body').text)
        # тут любой код для работы на странице
        # тут любой код для работы на странице
        # тут любой код для работы на странице
        # тут любой код для работы на странице
        # тут любой код для работы на странице
        time.sleep(2)


driver = uc.Chrome()
driver.get('https://www.youtube.com/')

