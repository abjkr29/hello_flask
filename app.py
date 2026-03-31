#플라스크 필요한거 가져오기
from flask import Flask
#플라스크 앱 만들기
app = Flask(__name__)

#'/'주소로 접속하면 실행됨
@app.route('/')
def home():
    return "Hello world!"

#이 파일을 실행했을때만 나옴
if __name__ == '__main__':
    app.run(debug=True)