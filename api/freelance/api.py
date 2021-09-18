from bs4 import BeautifulSoup
import requests


def main():
    projects = []
    while True:
        page_index = 1
        url = 'https://freelance.ru/project/search/pro?page=' + str(page_index)
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')

        project_list = soup.find('div', class_= 'projects').find_all('div', class_= 'project')
        for project in project_list:
            if 'pad' in project['class']:
                continue

            title = project.find('h2', class_= 'title').find('a').text.strip()
            href_fullpage = project.find('h2', class_= 'title').find('a').get('href')
            description = project.find('a', class_= 'description').text.strip()
            price = project.find('div', class_= 'cost').text.strip()
            term = project.find('div', class_= 'term').text.strip()

            title = ' '.join(title.split())
            description = ' '.join(description.split())
            price = ' '.join(price.split())
            term = ' '.join(term.split())

            projects.append({
                'from': 'freelance',
                'title': title,
                'href': href_fullpage,
                'description': description,
                'price': price,
                'term': term,
                'author': None
            })

        next_page = soup.find('ul', class_= 'pagination').find('li', class_= 'next')
        # if 'disabled' in next_page['class']:
        #     break

        # else:
        #     page_index += 1
        break
    print(projects)

        
    

if __name__ == '__main__':
    main()