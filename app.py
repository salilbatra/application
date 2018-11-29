from browser import Browser

if __name__=='__main__':
  import threading
  bro = Browser('http://www.zillow.com')
  threading.Thread(target=lambda: bro.revisit_url()).start()
  # bro.revisit_url()
