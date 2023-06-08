from flask_sqlalchemy import SQLAlchemy

# Create a DB object from the SQLAlchemy class

DB = SQLAlchemy()

class User(DB.Model):
    #id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    #username column
    username = DB.Column(DB.String, nullable=False)
    # backref is as if we had adde4d a tweets list to the user class
    # tweets = []

    def __repr__(self):
        return f"User: {self.username}"

class Tweet(DB.Model):
    #id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    #text column
    text = DB.Column(DB.Unicode(300))
    #user id column (foreign/secondary key)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    # user column creates a two-way link between a user object and a tweet
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return f"Tweet: {self.text}"