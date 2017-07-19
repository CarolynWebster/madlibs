"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment_list = sample(AWESOMENESS, 3)

    return render_template("greeting.html",
                           person=player,
                           compliments=compliment_list)



@app.route('/game')
def show_madlib_form():
    """Loads template based on if user want to play"""

    play_status = request.args.get("wants_to_play")

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    if play_status == "yes":
        return render_template("game.html", color_list=colors)
    else: #they said no
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Combines user input with madlib"""
    form_noun = request.args.get("noun")
    form_person = request.args.get("person")
    form_adj = request.args.getlist("adj")
    form_color = request.args.get("color")
    
    return render_template('madlib.html', 
                            lib_noun=form_noun, 
                            lib_person=form_person, 
                            lib_adj=form_adj, 
                            lib_color=form_color)


if __name__ == '__main__':
    
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
