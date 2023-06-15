from sklearn.linear_model import LogisticRegression
import numpy as np
from .models import User
from .twitter import vectorize_tweet

def predict_user(user0_username, user1_username, hypo_tweet_text):
    # Grad the users from the DB
    user0 = User.query.filter(User.username==user0_username).one()
    user1 = User.query.filter(User.username==user1_username).one()

    # Get the word embeddings from each user
    user_0vects = np.array([tweet.vect for tweet in user0.tweets])
    user_1vects = np.array([tweet.vect for tweet in user1.tweets])

    # Vertically stack the two 2D numpy arrays to make our X matrix
    X_train = np.vstack([user_0vects, user_1vects])

    # concatentate our labels of 0 or 1 for each tweet

    zeros = np.zeros(user_0vects.shape[0])
    ones = np.ones(user_1vects.shape[0])

    y_train = np.concatenate([zeros, ones])

    # Instantiate and fit a logisitic regression model
    log_reg = LogisticRegression().fit(X_train, y_train)

    # vectorize the hypothetical tweet
    hypo_tweet_vect = vectorize_tweet(hypo_tweet_text).reshape(1, -1)

    return log_reg.predict(hypo_tweet_vect)[0]
