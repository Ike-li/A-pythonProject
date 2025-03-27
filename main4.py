from urllib import request

response = request.urlopen("https://www.bing.com")
with response:
    print(response.geturl())
    print(response.getheaders())
