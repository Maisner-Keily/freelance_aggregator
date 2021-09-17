from bs4 import BeautifulSoup
import requests

def main():
    url = 'https://kwork.ru/projects'
    page = requests.get(url).text
    soup = BeautifulSoup(page)


if __name__ == '__main__':
    main()