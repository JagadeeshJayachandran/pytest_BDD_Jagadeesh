# Fixtures
import sys

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def browser():
    # b = webdriver.Chrome(ChromeDriverManager().install())
    print("********************")
    print(request.config.workerinput["mainargv"].sys.argv)
    b = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    b.implicitly_wait(10)
    yield b
    b.quit()



    # sadfsf
