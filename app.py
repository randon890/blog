from flask import Flask
import random
app = Flask(__name__)
facts = ["моя любимая игра no man sky", "мой любимый цвет чёрный","пантера"]
@app.route("/")
def hello_world():
    # return f'{random.choice(facts)}'
    # return "hello"
    return "Hi, I m Ilyas. How are you? I m doing well. <br> Today I had a good lesson. vvvb !"
app.run(debug=True)
# ctrl + s сохранит файл ctrl + c остановит веб сервер стрелочка наверхэто взят придучую команду из терменала,05