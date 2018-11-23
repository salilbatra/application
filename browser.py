class Browser:
  def open_browser(self, url):
    import webbrowser
    brow = webbrowser.get('firefox').open(url, new=1, autoraise=True)
    #brow.open(url, new=1, autoraise=True)
