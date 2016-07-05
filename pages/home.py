from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(Page):
    _search_textbox = (By.NAME, 'search_query')
    _search_button = (By.ID, 'search-btn')
    _result_list = (By.ID, 'results')

    @property
    def page_title(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.selenium.title)
        return self.selenium.title

    def search_for(self, keyword_to_search):
        self.find_element(*self._search_textbox).send_keys(keyword_to_search)
        self.find_element(*self._search_button).click()
        self.wait.until(EC.visibility_of_element_located(self._result_list))
