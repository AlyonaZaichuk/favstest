from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363'
driver.get(base_url)
driver.maximize_window()
add_to_favorites = driver.find_element(By.XPATH, "//*[@id='app']/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button/span")
add_to_favorites.click()

