from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def form():
    return render_template('syllabifier.html')


if __name__ == '__main__':
    app.run()
