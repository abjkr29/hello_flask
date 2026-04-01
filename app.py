from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 여기에 내 데이터를 만든다!
    my_profile = {
        "name": "안수현",
        "age": 19 ,
        "hobby": "게임",
        "favorite_food": "라면",
        "email:": "abjkr29@gmail.com"
    }

    return render_template('index.html', data=my_profile)

if __name__=='__main__':
    app.run(debug=True)