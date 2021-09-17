from bs4 import BeautifulSoup
import requests

def main():
    url = 'https://kwork.ru/projects'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    count_pages = int(soup.find('div', class_ = 'paging').find_all('li')[-2].text)
    projects = []
    for i in range(1, count_pages+1):
        url = 'https://kwork.ru/projects?page=' + str(i)
        print(url)
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        projects_list = soup.find('div', class_ = 'project-list').find_all('div', class_ = 'card')

        for project in projects_list:
            title = project.find('div', class_= 'wants-card__header-title').text
            href_fullpage = project.find('div', class_= 'wants-card__header-title').find('a').get('href')
            
            description = project.find('div', class_= 'wants-card__description-text br-with-lh').find('div', class_= 'js-want-block-toggle-full')
            if description != None:
                try:
                    toggleView = description.find('a')
                    toggleView.decompose() 
                    description = description.text
                except:
                    pass
            else:
                description = project.find('div', class_= 'wants-card__description-text').text

            price = project.find('div', class_= 'wants-card__header-price')
            price_spans = price.find_all('span')
            for span in price_spans:
                span.decompose()
            price = price.text
            
            author = project.find('div', class_= 'want-payer-statistic').find('a')
            author_href = author.get('href')
            author_name = author.text

            projects.append({
                'from': 'kwork',
                'title': title,
                'href': href_fullpage,
                'description': description,
                'price': price,
                'author': {
                    'name': author_name,
                    'href': author_href
                }
            })

    return projects

if __name__ == '__main__':
    main()