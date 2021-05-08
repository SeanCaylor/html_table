from flask import Flask, render_template
app = Flask(__name__)

users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


@app.errorhandler(404)
def not_found(e):
    return "I'm afraid I can't let you do that, Star Fox"

@app.route('/')
def index_main():
    return render_template('index.html', users = users)

if __name__ == "__main__":
    app.run(debug = True)