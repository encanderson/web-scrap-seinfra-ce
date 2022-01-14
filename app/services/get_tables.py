from bs4 import BeautifulSoup


def get_table(html):
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table')

    return table
