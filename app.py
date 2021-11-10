from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def form():
    return render_template('syllabifier.html')


@app.route('/', methods=['POST'])
def response():
    if request.method == 'POST':
        form_data = request.form
        return render_template('syllabified.html', form_data=form_data)

if __name__ == '__main__':
    app.run()
    #app.run(host='localhost', port=5000)
