import webbrowser
w = input("검색을 어디서 하나요?(구글, 네이버) : ")
s = input("검색할 것을 적으시오 :")
if (w == "구글"):
    url = "https://www.google.com/search?q="+s
    webbrowser.open(url)
elif (w == "네이버"):
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="+s
    webbrowser.open(url)