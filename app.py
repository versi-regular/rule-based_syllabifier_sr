from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def form():
    return render_template('syllabifier.html')


@app.route('/', methods=['POST'])
def response():
    if request.method == 'POST':
        form_data = request.form
        for _, value in form_data.items():
            text = value
        return render_template('syllabifier.html', text=text)

if __name__ == '__main__':
    app.run()
    #app.run(host='localhost', port=5000)
