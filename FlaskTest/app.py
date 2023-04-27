from js_wework import find_wework_jobs
from js_utils import print_jobs


from flask import Flask, render_template, request # 플라스크, 렌더, 리퀘스트
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/search')
def search():
    keyword_value = request.args.get('keyword') #콘솔에 get 방식으로 받은 내용 딕셔너리 형식으로 값 찍기
    if keyword_value:
        results = []
    temp = find_wework_jobs(keyword_value)
    if temp:
        results += temp

    print("")
    print_jobs(results)

    return render_template('search.html', keyword= keyword_value)