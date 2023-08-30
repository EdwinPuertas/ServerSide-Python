from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')

@app.route('/person_update/<id_person>', methods=['GET'])
def person_update(id_person):
    return render_template('person_update.html', id_person=id_person)

@app.route('/person_detail', methods=['POST'])
def person_detail():
    op = request.form['op']
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    print(model)
    if op == 'I':
        model.append(p)
    elif op == 'U':
        for row in model:
            if row.id_person == id_person:
                row.name = first_name
                row.last_name = last_name
                break
    print(model)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)

@app.route('/person_delete/<id_person>', methods=['GET'])
def person_delete(id_person):
    for i in range(0, len(model)):
        if model[i].id_person == id_person:
            model.pop(i)
    data = [(i.id_person, i.name, i.last_name) for i in model]
    return render_template('people.html', value=data)


if __name__ == '__main__':
    app.run()