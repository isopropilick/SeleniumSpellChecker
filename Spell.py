import re, collections, html5lib
from selenium import webdriver
from bs4 import BeautifulSoup
from enchant import DictWithPWL
from enchant.checker import SpellChecker
#                      ---- Inicia selenium ----
driver = webdriver.Firefox ()
url = "file:///C:/Users/QUALITY/Desktop/tst.html"
driver.get(url)
rawHTML = driver.page_source
driver.quit()
#                      ---- Termina selenium (codigo html declarado en rawHTML) ----
#                      ---- Inicia extraccion de texto ----
soup = BeautifulSoup(rawHTML, "html5lib")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text().encode('utf-8')
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("\n"))
text = "\n".join(chunk for chunk in chunks if chunk)
#                      ---- Termina extraccion de texto (declarada en text) ----
#                      ---- Inicia "formateo de header de archivo de texto" ----
f = open ("c:/1/test.txt", "w")
f.write("Reporte de errores ortograficos.\n--------------------------------------\nObtenido de:  ")
f.write(url)
f.write("\n--------------------------------------\n\n")
#                      ---- Termina "formateo de header de archivo de texto" ----
#                      ---- Inicia "impresion de errores ortograficos" ----
dic = DictWithPWL("es_MX")
chkr = SpellChecker(dic)
chkr.set_text(text)
for error in chkr:
    f.write("*")
    f.write(error.word)
    f.write("\n")
f.close ()
#                      ---- Termina "impresion de errores ortograficos" se cierra .txt ----
