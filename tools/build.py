"""Build index.html and the iPhone version from the main file: python3 tools/build.py"""
import shutil
src = "Aegis Order Flow.html"
shutil.copyfile(src, "index.html")
s = open(src, encoding="utf-8").read()
def rep(a, b):
    global s
    assert a in s, a[:80]
    s = s.replace(a, b)
rep("@media (max-width:1100px){", "@media all{")          # phone layout always on
rep("@media (max-width:760px){", "@media all{")
rep("<title>Aegis Order Flow</title>", "<title>Aegis Order Flow iPhone</title>")
s = s.replace('"afe.settings"', '"afe.iphone.settings"').replace('"afe.userLevels"', '"afe.iphone.userLevels"')
s = s.replace("innerWidth <= 1100", "true")                  # book chip always on
open("Aegis Order Flow iPhone.html", "w", encoding="utf-8").write(s)
open("phone.html", "w", encoding="utf-8").write(s)   # short link: /phone.html
shutil.copyfile(src, "pc.html")                         # short link: /pc.html
print("built index.html, pc.html, phone.html, Aegis Order Flow iPhone.html")
