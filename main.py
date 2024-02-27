from flask import Flask, render_template
from database import load_data_from_db

app = Flask(__name__)


@app.route('/')
def index():
  data = load_data_from_db()
  return render_template('home.html', data = data, debug=True)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
