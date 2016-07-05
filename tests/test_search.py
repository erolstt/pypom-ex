import pytest
from pages.home import HomePage


@pytest.mark.nondestructive
def test_could_search(base_url, selenium):
    page = HomePage(selenium, base_url).open()
    page.search_for('ChessNetwork')
    assert 'ChessNetwork - YouTube' == page.page_title
