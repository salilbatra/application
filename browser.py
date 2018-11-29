class Browser:

  def __init__(self, url):
  	self.url = url

  def open_browser(self):

    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.keys import Keys

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    open_window = webdriver.Firefox(firefox_profile=firefox_profile)
    open_window.get(self.url)
    sleep(15)
    open_window.close()

  def revisit_url(self):
  	import random, time, traceback

  	next_time = time.time() + random.randint(10, 20)
  	while True:
  		time.sleep(max(0, next_time - time.time()))
  		try:
  			self.open_browser()
  		except Exception as e:
  			traceback.print_exc()
  		
  		next_time += (time.time() - next_time)