import urllib

def get_page(url):
    source = urllib.urlopen(url)
    print source.read();
    return source.read();


get_page("http://www.google.com");