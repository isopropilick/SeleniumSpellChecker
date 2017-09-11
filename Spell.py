from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Firefox ()
url = "http://192.168.1.201:8189/evaluaciones/login"
driver.get(url)
elementos = driver.page_source
driver.quit()
soup = BeautifulSoup(elementos, "lxml")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text().encode('utf-8')
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("\n"))
text = "\n".join(chunk for chunk in chunks if chunk)
text = text.strip()
f = open ("c:/1/test.txt", "w")
f.write(text)
f.close ()
