from flask import Flask
app = Flask(__name__)
code = """
    <h1>Добро пожаловать в мой блог</h1>
    <p>моя любимая игра <b>no man sky</b></p>
    <p>моя любимая игра <i>atomic heart</i></p>
    <p>моя любимая игра <b>strafe</b></p>
    <a href="https://randomcolour.com/">нажми меня</a>
    <a href="https://habrastorage.org/getpro/habr/upload_files/a88/3f1/2b4/a883f12b4ea1eb36e63020edea94a3d9.jpg">нажми меня</a>
    <img src="https://image.api.playstation.com/vulcan/ap/rnd/202508/2714/518b690d5e17ce7aba2d9917bd5b81c309065a510170ec52.jpg" alt="no man sky" width=800px height=500px>
"""
@app.route("/")
def main_page():
    return code
app.run(debug=True)