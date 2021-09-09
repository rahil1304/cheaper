from json import encoder
from selenium import webdriver
from bs4 import BeautifulSoup
import json

data = {}

driver = webdriver.PhantomJS(executable_path="phantomjs")
# item = input("Enter Item: ")
item = 'table'
data[item] = []
URL = 'https://www.amazon.com/s?k=' + item + '&ref=nb_sb_noss_2'
driver.get(URL)

html = driver.execute_script("return document.documentElement.innerHTML;")
soup = BeautifulSoup(html, features="html.parser")

# print(str(soup))

itemName = []
itemPrice = []
numberOfResults = len(soup.find_all(attrs={"class": "a-section a-spacing-none"}))


for i in soup.find_all(attrs={"class": "a-section a-spacing-none"}):
    product = {}
    for j, k in zip(i.find_all_next(attrs={"class": "a-size-base-plus a-color-base a-text-normal"}), i.find_all_next(attrs={"class": "a-offscreen"})):
        product['Name'] = j.text
        product['Price'] = k.text
    # for j in i.find_all_next(attrs={"class": "a-offscreen"}):
    #     itemPrice.append(j.text)
    data[item].append(product)


file1 = open("results.json", "w", encoding='UTF-8')
json.dump(data, file1, ensure_ascii=False)

# for i in range(numberOfResults):
#     row = str(itemName[i]) + ": " + str(itemPrice[i])
#     print(row)
#     file1.write(row)