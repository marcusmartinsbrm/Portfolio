import webdriver

with webdriver.Session("127.0.0.1", 4444) as session:
    session.url = "https://mozilla.org"
    print "The current URL is %s" % session.url