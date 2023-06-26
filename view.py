import datetime
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.context_processor
def inject_today_date():
    now = datetime.datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    return {'today_date': date_time_str}

@app.route('/index')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)