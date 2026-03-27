from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
url = "https://test2023.bsmu.by/login/"


try:
    driver.get(url=url)
    time.sleep(3)
    login_name_input = driver.find_element(By.ID, "username")
    login_name_input.clear()
    login_name_input.send_keys("hotait")
    time.sleep(3)
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys("Andrei13")
    time.sleep(3)
    loggin_button = driver.find_element(By.ID, "loginbtn").click()
    time.sleep(3)
    # with open("tests.txt", "w") as document:
    #     document.write("Основные тесты по ортодонтии\n\n")
    for page in range(0, 483, 1):
        driver.get(f"https://test2023.bsmu.by/mod/quiz/attempt.php?attempt=64177&cmid=75&page={page}")
        # https://test2023.bsmu.by/mod/quiz/attempt.php?attempt=53872&cmid=75&page=1
        time.sleep(1)
        # отвечаем на второй вариант
        # try:
        #     driver.find_element(By.ID, f"q64240:{page + 1}_answer1").click()
        #     time.sleep(1)
        #     driver.find_element(By.ID, f"q64240:{page + 1}_-submit").click()
        # except NoSuchElementException:
        #     print("Элемент не найден")
        # try:
        #     driver.find_element(By.ID, f"q64240:{page + 1}_choice1").click()
        #     time.sleep(1)
        #     driver.find_element(By.ID, f"q64240:{page + 1}_-submit").click()
        # except NoSuchElementException:
        #     print("Элемент не найден")
        # time.sleep(1)
        # делаем сприншот
        # driver.save_screenshot(f'photo/{page + 1}.png')
        # записываем вопросы в файл
        question = driver.find_element(By.CLASS_NAME, "qtext").text
        answer = driver.find_element(By.CLASS_NAME, "answer").text
        rightanswer = driver.find_element(By.CLASS_NAME, "rightanswer").text
        with open("tests.txt", "a") as document:
            document.write(f"Вопрос {page + 1}: {question}\n{answer}\n{rightanswer}\n\n")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


