from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def helloword():
    msg = " hello guys !  welcome to the flask"
    return msg


if __name__ == '__main__':
    app.run(debug=False)
