from flask import Flask, render_template
import requests
import boto3
app = Flask(__name__)
@app.route('/')
def index():
    names = ['Adityan','aathil','kannan','rajeswari']
    date = []
    for i in names:
        url = "https://t14nk6pof9.execute-api.us-east-2.amazonaws.com/sanitizerappretrieve?Name="+i
        resp = requests.get(url)
        data = resp.json()
        print(data)
        date.append(data['date'])
    return render_template('stats.html', p1= names[0],d1=date[0], p2=names[1], d2=date[1],p3=names[2], d3=date[2],p4=names[3], d4=date[3])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)