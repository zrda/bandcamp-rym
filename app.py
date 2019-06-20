from flask import Flask, request, render_template
import os
import scrape
import infotext

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    output = scrape.format(request.form['url'])
    return render_template('index.html', output=output)

@app.route('/info/')
def info():
    message = infotext.contents()
    return render_template('info.html', message=message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
