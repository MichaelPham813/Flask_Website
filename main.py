from flask import Flask, render_template, request
from weather_check import get_weather
from bmi_calculator import bmi_calculators
from ISS_data import ISS_dataset
from ISS_location import get_location
import json
app = Flask('app')

user_lat = None
user_lon = None
#Call in weather API and weather function
weather = get_weather(46.493919,-80.995415)
celcius_temp = round(weather['main']['temp'] - 273.15,2)
desc = weather['weather'][0]
description = desc['description']






#Home/Default page
@app.route('/')
def Home():     
  return render_template("index.html")

#About page
@app.route('/about/')
def About():
  return render_template("about.html")





#Education page
@app.route('/education/')
def Edu():
  return render_template("education.html")

#Experience page
@app.route('/experience/')
def Exp():
  return render_template("experience.html")

#Contact page
@app.route('/contact/')
def Contact():
  return render_template("contact.html")

#Weather page
@app.route('/weather/')
def Weather():
  return render_template("weather.html",weather=description,temp=celcius_temp)

#BMI page
@app.route('/bmi/', methods = ['GET','POST'])
def BMI():
  if request.method == "POST":
      height_str = request.form.get('height')
      weight_str = request.form.get('weight')
      bmi_type,bmi_number = bmi_calculators(height_str,weight_str)
      bmi_data = {'bmi_type':bmi_type,"bmi_number":bmi_number}
      with open("bmi.json","w") as f:
        json.dump(bmi_data,f)
      return render_template("bmi.html",bmi_type=bmi_type,bmi_number = bmi_number) 

  return render_template("bmi.html")




@app.route('/ISS_Location/')
def ISS_loc():
  dataset = ISS_dataset()
  location = get_location()
  temp,desc,country,overWater,distance,flag = dataset[0],dataset[1],dataset[2],dataset[3],dataset[4],dataset[5]
  lat,lon = location[0],location[1]
  return render_template("ISS_Location.html",temp=temp,desc=desc,country=country,overWater=overWater,distance=distance,flag=flag,lat=lat,lon=lon)


@app.route('/user_loc',methods = ['POST'])
def user_loc():
  data = request.get_json()
  user_lat = data[0]
  user_lon = data[1] 
  print(user_lat,user_lon)
  lat_user = json.loads(user_lat)
  lon_user = json.loads(user_lon)
  return lat_user,lon_user


app.run(host='0.0.0.0', port=5000)