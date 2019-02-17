from flask import Flask, request, render_template
import scrape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    output = scrape.format(request.form['url'])
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run()
