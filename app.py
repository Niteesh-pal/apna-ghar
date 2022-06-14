import os
from random import choice
from flask import Flask, render_template,url_for

app = Flask(__name__)

area=['Lucknow','Delhi','Punjab','Noida','Rajastan','Haryana','Mumbai']
desc=['Have a look on this building. This might be your dream home.','This is our famous home, were u can find everything,have a look ','Hey does you have a home?..then just find one here!','pls check out this home you may admire its beauty','check out this one........it a having a wonderful','i really like ur body ...let me do some party ']
link=['Lucknow','Delhi']

facility=['Ambulance','Movie theater','gym','Mall','swimming pool']

fac_desc=['There is a nearby hospital for emergency In some instances, out-of-hospital medical care is provided to the patient.',"Nothing can beat the experience of watching a movie in a theatre. It's a different and a special experience all-together.",'Gyms and fitness facilities provide an important outlet for people seeking to improve their health and well-being.we provide u every gym kit',' Mall management encompasses operations, facilities management, security, common area maintenance, leasing and all the other functions.','Swimming pools in remote communities also provide children with the opportunity to learn valuable lifesaving swimming skills']
@app.route('/')
def hello_world():
    names = os.listdir('static/imgs')
    names = ['imgs/'+ image for image in names]
    l=len(names)

    fac = os.listdir('static/fac')
    fac = ['fac/'+ image for image in fac]
    count=0
    return render_template('home.html', names_area_desc=zip(names,area,desc), sndloop=zip(fac,facility,fac_desc),count=count)



@app.route('/login')
def rough():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/<names>')
def display(names):
    Lucknow = os.listdir('static/Lucknow')
    Lucknow = ['Lucknow/'+ image for image in Lucknow]

    detail=['evi','Bedroom','Garden','Hall','Guest room ','Kitchen']
    lko_detl=['Room for rent in , Indira Nagar ',' Residential House for Rent in Greater Kailash','1 BHK House for rent in Punjabi Bagh East','3 BHK Independent House for rent in Ibadullapur, Greater Noida','4 Bedroom House for rent in Vaishali Nagar,Rajasthan']
    price=['30,000 per annum','20,000 per annum','40,000 per annum','1 lakh per annum','60,000 per annum']              
               

    if names=="Lucknow":
        return render_template('display.html',names=names,loc=Lucknow,detail=detail,lko_detl=lko_detl,price=price)

    elif names=="Delhi":
        Delhi = os.listdir('static/Delhi')
        Delhi = ['Delhi/'+ image for image in Delhi]
        return render_template('display.html',names=names,loc=Delhi,detail=detail,lko_detl=lko_detl,price=price)

    elif names=="Punjab":
         Punjab= os.listdir('static/Punjab')
         Punjab = ['Punjab/'+ image for image in Punjab]
         return render_template('display.html',names=names,loc=Punjab,detail=detail,lko_detl=lko_detl,price=price)

    elif names=="Noida":
        Noida = os.listdir('static/Noida')
        Noida = ['Noida/'+ image for image in Noida]
        return render_template('display.html',names=names,loc=Noida,detail=detail,lko_detl=lko_detl,price=price)

    else:
        Rajasthan = os.listdir('static/Rajasthan')
        Rajasthan = ['Rajasthan/'+ image for image in Rajasthan]
        return render_template('display.html',names=names,loc=Rajasthan,detail=detail,lko_detl=lko_detl,price=price)



    
    
@app.route('/fac/<names>')
def faci(names):
    return render_template('fac.html',names=names,details=fac_desc)

if __name__ == "__main__":
    app.run(debug=True)