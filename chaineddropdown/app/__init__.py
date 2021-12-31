
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import jinja_partials
app = Flask(__name__)

app.config.from_object("config")
db = SQLAlchemy(app)
jinja_partials.register_extensions(app)

@app.route('/')
@app.route('/index.html')
def index():
    provinces = db.session.execute("SELECT * FROM province order by code")
    return render_template('index.html', provinces=provinces)

@app.route('/cities/', methods=['GET'])
def get_cities():
    province = request.args.get("province")
    cities = db.session.execute("SELECT * FROM city WHERE provinceCode=:province",{"province":province}) 
    return render_template("partials/cities.html", cities=cities)

@app.route('/areas/', methods=['GET'])
def get_areas():
    city = request.args.get("city")
    areas = db.session.execute("SELECT * FROM area WHERE cityCode=:city",{"city":city})
    return render_template("partials/areas.html", areas=areas)



