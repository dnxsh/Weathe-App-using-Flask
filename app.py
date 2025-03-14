from flask import Flask,render_template,request
import requests
app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        city_name=request.form['City']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=39a788a382724ea022a6df21e3534a6b&units=metric'
        response=requests.get(url).json()
        city= city_name
        temp= str(response['main']['temp'])+'°C'
        desc= response['weather'][0]['description'].capitalize()
        hum= str(response['main']['humidity'])+'%'
        wind= str(response['wind']['speed'])+'m/s'
        icon= response['weather'][0]['icon']
        return render_template('index.html',city=city,temp=temp,desc=desc,hum=hum,wind=wind,icon=icon)
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
