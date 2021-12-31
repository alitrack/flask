
from flask import Flask, render_template, request,render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object("config")
db = SQLAlchemy(app)

@app.route('/')
@app.route('/index.html')
def index():
    provinces = db.session.execute("SELECT * FROM province order by code")
    return render_template('index.html', provinces=provinces)

@app.route('/cities/', methods=['GET'])
def get_cities():
    templ = """
    {%for city in cities %}
        <option value="{{ city.code }}">{{ city.name }}</option>
    {% endfor %}
    """
    province = request.args.get("province")
    cities = db.session.execute("SELECT * FROM city WHERE provinceCode=:province",{"province":province}) 
    return render_template_string(templ, cities=cities)

@app.route('/areas/', methods=['GET'])
def get_areas():
    templ = """
    {%for area in areas %}
        <option value="{{ area.code }}">{{ area.name }}</option>
    {% endfor %}
    """
    city = request.args.get("city")
    areas = db.session.execute("SELECT * FROM area WHERE cityCode=:city",{"city":city})
    return render_template_string(templ, areas=areas)


