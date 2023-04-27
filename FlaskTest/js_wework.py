import requests
from bs4 import BeautifulSoup

def find_wework_jobs(keyword):  #키워드 받음
  base_url = "https://weworkremotely.com/remote-jobs/search?term="  #url양식
  res = requests.get(f"{base_url}{keyword}")  #request 요청
  if res.status_code != 200:  #만약 제대로 통신이 안되었다면
    print(f"Http Response Error: {res.status_code}")  #오류 http 코드 전송
    return

  results = []  #결과 딕셔너리
  soup = BeautifulSoup(res.content, 'html.parser')  #크롤링 시작
  job_sections = soup.find_all('section', class_='jobs')  #세부 크롤링 시작
  for job_section in job_sections:
    job_posts = job_section.find_all('li')
    job_posts.pop(-1)
    for job in job_posts:
      link = job.a['href']
      company, _, location = job.find_all(class_='company')
      title = job.find(class_='title')
      job_post = {
        "link": f"https://weworkremotely.com{link}",
        "company": company.string,
        "title": title.string,
        "location": location.string
      }
      results.append(job_post)

  return results  #객체 리턴