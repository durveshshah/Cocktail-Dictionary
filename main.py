import requests
from flask import Flask, render_template,request


app =Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

@app.route('/search',methods = ['POST'])
def getalcohol():
    if request.method == 'POST':
        value = request.form['search']
        print("value", value)
        api_url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={value}'
        print('api_url' ,api_url)
        try:
            r = requests.get(api_url)
            data = r.json()
            print('data',data)
            array = data["drinks"]
            print('array ', array)
            return render_template("cocktail_data.html",array=array,value=value)
        except:
            return " <h1> Oops.. No such cocktail found </h1>"

@app.route('/search/<type>',methods=['GET', 'POST'])

# Getting clicked data from url we used get
def cocktail_select(type):
    selected_cocktail = type
    if request.method == 'GET':
        new_url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={selected_cocktail}'
        print('api_url 1', new_url)
        try:
            r = requests.get(new_url)
            data = r.json()
            print('data', data)
            array = data["drinks"]
            return render_template("cocktail_home.html", array=array,selected_cocktail=selected_cocktail,
                                   )
        except:
            return "Unexpected Error Occurred"

if __name__ == '__main__':
    app.run(debug = True)

