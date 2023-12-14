#i will take a input, call the API, and return the result === this is the code we are going to do her

from flask import Flask, render_template, request
import requests                 #request and requests these are two?  request is to get the data from the form. and requests is to get the data from the URL, basically the data from API

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

#writing a function, which will take all 3 data(for here), execute an API, and return the result
@app.route("/weatherapp", methods= ['POST', "GETS"])   #at this route.(this route name you have mentioned in you html code.)/////methods wala bas nhi samajh rha hai. kya hai post get blah blah.
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param= {
        'q': request.form.get("city"),
        'appid': request.form.get("appid"),
        'units':request.form.get('units')
    }

    response = requests.get(url, params=param)
    city=data['name']                                                      #new changes                     #why is this data mentioned before the data variable?
    data = response.json()
    return f"data: {data} , city : {city}" #returning the json data to the user.,        #new changes.

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 5002)