from selenium import webdriver

options = webdriver.ChromeOptions()
# options.page_load_strategy = "eager"
# options.add_argument("--headless=new")
prefs = {
    "profile.managed_default_content_settings.images": 2,
}
options.add_experimental_option("prefs", prefs)
