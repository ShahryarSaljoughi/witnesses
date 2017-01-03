from flask import Flask
from flask_oauthlib.client import OAuth


app = Flask(__name__)
oauth = OAuth()
twitter = oauth.remote_app(
    name='twitter',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    consumer_key='QzEPgFE48YNlQ6CJOIfw3dHPp',
    consumer_secret='Y0gJjoOFsDTugctsDaukHfwvaEFZJM0OQ7E7bFiWw8I8sYUvEU'
)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


# OAuth
def obtain_request_token():
    pass
