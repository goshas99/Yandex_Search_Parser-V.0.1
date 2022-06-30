from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import time


def main():
    request = input('Введите запрос: ')
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.implicitly_wait(10)
    driver.get(f'https://yandex.ru/search/?text={request}&lr=213&within=77')
    time.sleep(15)
    try:
        one = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[1]')
        header1 = one.find_element(By.XPATH, '//*[@id="search-result"]/li[1]/div/div[1]/a/h2/span').text
        desc1 = one.find_element(By.XPATH, '//*[@id="search-result"]/li[1]/div/div[3]/div[1]/span/label/span[2]').text
        link1 = one.find_element(By.XPATH, '//*[@id="search-result"]/li[1]/div/div[2]/div[1]/a').text
    except:
        pass
        # one = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[1]')
        # header1 = one.find_element(By.XPATH, '//*[@id="search-result"]/li[1]/div/div[1]/div[1]/a/h2/span').text
        # desc1 = one.find_element(By.XPATH, '//*[@id="search-result"]/li[1]/div/div[1]/div[3]/div/span').text
        # link1 = one.find_element(By.XPATH, '//*[@id="search-result"]/li[1]/div/div[1]/div[2]/div[1]/a').text
    try:
        two = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[2]')
        header2 = two.find_element(By.XPATH, '//*[@id="search-result"]/li[2]/div/div[1]/a/h2/span').text
        desc2 = two.find_element(By.XPATH, '//*[@id="search-result"]/li[2]/div/div[3]/div/span/label/span[2]').text
        link2 = two.find_element(By.XPATH, '//*[@id="search-result"]/li[2]/div/div[2]/div[1]/a').text
    except:
        pass
        # two = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[2]')
        # header2 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[2]/div/div[1]/div[1]/a/h2/span').text
        # desc2 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[2]/div/div[1]/div[3]/div/span').text
        # link2 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[2]/div/div[1]/div[2]/div[1]/a').text
    try:
        three = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[3]')
        header3 = three.find_element(By.XPATH, '//*[@id="search-result"]/li[3]/div/div[1]/a/h2/span').text
        desc3 = three.find_element(By.XPATH, '//*[@id="search-result"]/li[3]/div/div[3]/div/span/label/span[2]').text
        link3 = three.find_element(By.XPATH, '//*[@id="search-result"]/li[3]/div/div[2]/div[1]/a/b').text
    except:
        pass
        # three = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[3]')
        # header3 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[3]/div/div[1]/div[1]/a/h2/span').text
        # desc3 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[3]/div/div[1]/div[3]/div/span').text
        # link3 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[3]/div/div[1]/div[2]/div[1]/a').text
    try:
        four = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[4]')
        header4 = four.find_element(By.XPATH, '//*[@id="search-result"]/li[4]/div/div[1]/a/h2/span').text
        desc4 = four.find_element(By.XPATH, '//*[@id="search-result"]/li[4]/div/div[3]/div/span/label/span[2]').text
        link4 = four.find_element(By.XPATH, '//*[@id="search-result"]/li[4]/div/div[2]/div[1]/a/b').text
    except:
        pass
        # four = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[4]')
        # header4 = four.find_element(By.XPATH, '//*[@id="search-result"]/li[4]/div/div[1]/div[1]/a/h2/span').text
        # desc4 = four.find_element(By.XPATH, '//*[@id="search-result"]/li[4]/div/div[1]/div[3]/div/span').text
        # link4 = four.find_element(By.XPATH, '//*[@id="search-result"]/li[4]/div/div[1]/div[2]/div[1]/a').text
    try:
        five = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[5]')
        header5 = five.find_element(By.XPATH, '//*[@id="search-result"]/li[5]/div/div[1]/a/h2/span').text
        desc5 = five.find_element(By.XPATH, '//*[@id="search-result"]/li[5]/div/div[3]/div/span/label/span[2]').text
        link5 = five.find_element(By.XPATH, '//*[@id="search-result"]/li[5]/div/div[2]/div[1]/a').text
    except:
        pass
        # five = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[5]')
        # header5 = five.find_element(By.XPATH, '//*[@id="search-result"]/li[5]/div/div[1]/div[1]/a/h2/span').text
        # desc5 = five.find_element(By.XPATH, '//*[@id="search-result"]/li[5]/div/div[1]/div[3]/div/span').text
        # link5 = five.find_element(By.XPATH, '//*[@id="search-result"]/li[5]/div/div[1]/div[2]/div[1]/a').text
    try:
        six = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[6]')
        header6 = six.find_element(By.XPATH, '//*[@id="search-result"]/li[6]/div/div[1]/a/h2/span').text
        desc6 = six.find_element(By.XPATH, '//*[@id="search-result"]/li[6]/div/div[3]/div/span/label/span[2]').text
        link6 = six.find_element(By.XPATH, '//*[@id="search-result"]/li[6]/div/div[2]/div[1]/a').text
    except:
        pass
        # six = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[6]')
        # header6 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[6]/div/div[1]/div[1]/a/h2/span').text
        # desc6 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[6]/div/div[1]/div[1]/a/h2/span').text
        # link6 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[6]/div/div[1]/div[2]/div[1]/a').text
    try:
        seven = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[7]')
        header7 = seven.find_element(By.XPATH, '//*[@id="search-result"]/li[7]/div/div[1]/a/h2/span').text
        desc7 = seven.find_element(By.XPATH, '//*[@id="search-result"]/li[7]/div/div[3]/div/span/label/span[2]').text
        link7 = seven.find_element(By.XPATH, '//*[@id="search-result"]/li[7]/div/div[2]/div[1]/a').text
    except:
        pass
        # seven = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[7]')
        # header7 = seven.find_element(By.XPATH, '//*[@id="search-result"]/li[7]/div/div[1]/div[1]/a/h2/span').text
        # desc7 = seven.find_element(By.XPATH, '//*[@id="search-result"]/li[7]/div/div[1]/div[1]/a/h2/span').text
        # link7 = seven.find_element(By.XPATH, '//*[@id="search-result"]/li[7]/div/div[1]/div[2]/div[1]/a').text
    try:
        eight = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[8]')
        header8 = eight.find_element(By.XPATH, '//*[@id="search-result"]/li[8]/div/div[1]/a/h2/span').text
        desc8 = eight.find_element(By.XPATH, '//*[@id="search-result"]/li[8]/div/div[3]/div/span/label/span[2]').text
        link8 = eight.find_element(By.XPATH, '//*[@id="search-result"]/li[8]/div/div[2]/div[1]/a').text
    except:
        pass
        # eight = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[8]')
        # header8 = eight.find_element(By.XPATH, '//*[@id="search-result"]/li[8]/div/div[1]/div[1]/a/h2/span').text
        # desc8 = eight.find_element(By.XPATH, '//*[@id="search-result"]/li[8]/div/div[1]/div[1]/a/h2/span').text
        # link8 = eight.find_element(By.XPATH, '//*[@id="search-result"]/li[7]/div/div[1]/div[2]/div[1]/a').text
    try:
        nine = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[9]')
        header9 = nine.find_element(By.XPATH, '//*[@id="search-result"]/li[9]/div/div[1]/a/h2/span').text
        desc9 = nine.find_element(By.XPATH, '//*[@id="search-result"]/li[9]/div/div[3]/div/span/label/span[2]').text
        link9 = nine.find_element(By.XPATH, '//*[@id="search-result"]/li[9]/div/div[2]/div[1]/a').text
    except:
        pass
        # nine = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[9]')
        # header9 = nine.find_element(By.XPATH, '//*[@id="search-result"]/li[9]/div/div[1]/div[1]/a/h2/span').text
        # desc9 = nine.find_element(By.XPATH, '//*[@id="search-result"]/li[9]/div/div[1]/div[1]/a/h2/span').text
        # link9 = nine.find_element(By.XPATH, '//*[@id="search-result"]/li[9]/div/div[1]/div[2]/div[1]/a').text
    try:
        ten = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[10]')
        header10 = ten.find_element(By.XPATH, '//*[@id="search-result"]/li[10]/div/div[1]/a/h2/span').text
        desc10 = ten.find_element(By.XPATH, '//*[@id="search-result"]/li[10]/div/div[3]/div/span/label/span[2]').text
        link10 = ten.find_element(By.XPATH, '//*[@id="search-result"]/li[10]/div/div[2]/div[1]/a').text
    except:
        pass
        # ten = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[10]')
        # header10 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[10]/div/div[1]/div[1]/a/h2/span').text
        # desc10 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[10]/div/div[1]/div[1]/a/h2/span').text
        # link10 = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[10]/div/div[1]/div[2]/div[1]/a').text

    with open("yandex.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter="*")
        try:
            file_writer.writerow(
                ['Номер в поиске: 1', f'Заголовок: {header1}', f'Описание: {desc1}', f'Ссылка: {link1}'])
        except:
            pass
        file_writer.writerow('')
        try:
            file_writer.writerow(
                ['Номер в поиске: 2', f'Заголовок: {header2}', f'Описание: {desc2}', f'Ссылка: {link2}'])
        except:
            pass
        try:
            file_writer.writerow(
                ['Номер в поиске: 3', f'Заголовок: {header3}', f'Описание: {desc3}', f'Ссылка: {link3}'])
        except:
            pass
        file_writer.writerow('')
        try:
            file_writer.writerow(
                ['Номер в поиске: 4', f'Заголовок: {header4}', f'Описание: {desc4}', f'Ссылка: {link4}'])
        except:
            pass
        try:
            file_writer.writerow(
                ['Номер в поиске: 5', f'Заголовок: {header5}', f'Описание: {desc5}', f'Ссылка: {link5}'])
        except:
            pass
        file_writer.writerow('')
        try:
            file_writer.writerow(
                ['Номер в поиске: 6', f'Заголовок: {header6}', f'Описание: {desc6}', f'Ссылка: {link6}'])
        except:
            pass
        try:
            file_writer.writerow(
                ['Номер в поиске: 7', f'Заголовок: {header7}', f'Описание: {desc7}', f'Ссылка: {link7}'])
        except:
            pass
        file_writer.writerow('')
        try:
            file_writer.writerow(
                ['Номер в поиске: 8', f'Заголовок: {header8}', f'Описание: {desc8}', f'Ссылка: {link8}'])
        except:
            pass
        try:
            file_writer.writerow(
                ['Номер в поиске: 9', f'Заголовок: {header9}', f'Описание: {desc9}', f'Ссылка: {link9}'])
        except:
            pass
        file_writer.writerow('')
        try:
            file_writer.writerow(
                ['Номер в поиске: 10', f'Заголовок: {header10}', f'Описание: {desc10}', f'Ссылка: {link10}'])
        except:
            pass


if __name__ == "__main__":
    main()
