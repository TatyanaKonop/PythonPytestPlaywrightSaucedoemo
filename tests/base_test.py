import pytest

from utils.json_parser import JsonParser


@pytest.mark.usefixtures('pages')
class BaseTest:
    @pytest.fixture(autouse=True)
    def injector(self, pages):
        # instantiates pages object, and data readers
        self.pages = pages
        # self.config_reader = prep_properties
        self.json_reader = JsonParser("tests_data.json")
