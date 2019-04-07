import re
import requests
import urllib
import json
import urllib.request
from bs4 import BeautifulSoup

from core.models import University, ProgramHighlights


def create_highlights(univ_url, url='https://www.topmba.com'):

    response = requests.get(url + univ_url)
    soup = BeautifulSoup(response.text, "html.parser")

    keyset = {'Start Month': 'start_month', 'Class Size': 'class_size', 'Avg. Work Experience': 'avg_work_experience',
              'Avg. Student Age': 'avg_student_age', "Int'l Students": 'intl_students', 'Women Students': 'women_students',
              'Avg. Salary(Post 3 Months)': 'avg_salary', 'Scholarship': 'scholarship', 'Accreditations': 'accreditations'}

    tags = soup.findAll("div", class_="data-boxes")
    if response.status_code == 200:
        highlights = {}

        for field in tags:
            data = field.get_text()

            data = [obj for obj in data.split('\n') if obj]

            key = data[0]
            value = data[-1]

            if keyset.get(key, None):
                highlights[keyset[key]] = value

        highlight_obj = ProgramHighlights.objects.create(**highlights)

        return highlight_obj.id
    return None


def upload_data_to_db(url='https://www.topmba.com/sites/default/files/qs-rankings-data/330380.txt?_=1554441939161'):

    with urllib.request.urlopen(url) as response:

        keyset = {'city': 'cities',
                  'location': 'country', 'more': 'url'}
        universities = []

        values = json.load(response)

        for data in values['data']:

            university = {}

            title = data['title']

            university_name = title.split('</b><br />')[0][3:]
            university['university'] = university_name

            course_name = title.split('</b><br />')[1]
            university['course'] = course_name

            university['rank'] = re.findall(r'\d+', data['rank_display'])[0]

            for modelkey, responsekey in keyset.items():
                university[modelkey] = data[responsekey]
            highlight_id = create_highlights(data['url'])

            university['program_highlights_id'] = highlight_id

            universities.append(University(**university))

        uploaded_university_list = University.objects.bulk_create(
            universities)
