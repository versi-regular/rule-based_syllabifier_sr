from flask import Flask, render_template, request
from source.syllabifier import syllabify
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def syllabifier():
    if request.method == 'POST':
        form_data = request.form
        return render_template('base.html', text=syllabify(list(form_data.values())[0]))
    else:
        return render_template('base.html')


if __name__ == '__main__':
    app.run()
