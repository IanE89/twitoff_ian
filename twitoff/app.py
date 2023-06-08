from flask import Flask, render_template
from .models import DB, User, Tweet

def create_app():

    app = Flask(__name__)

    # database configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #register our database with the app
    DB.init_app(app)

    my_var = "Twitoff App"

    @app.route('/')
    def root():
        return render_template('base.html', title='Home')

    @app.route('/bananas')
    def bananas():
        return render_template('base.html', title='Bananas')
    
    @app.route('/reset')
    def reset():
        #Drop all database tables
        DB.drop_all()
        DB.create_all()
        return "database has been reset"

    return app