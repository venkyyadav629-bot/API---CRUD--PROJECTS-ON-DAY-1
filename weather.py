from flask import Flask

app = Flask(__name__)
@app.route('/')
def cool():
    return '<h1> Hey your first project successfully ronning on internet</h1>'
if __name__ == '__main__':
   app.run()
