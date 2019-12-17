## How to run commands on windows

from home directory

set FLASK_APP=APP
flask run

set FLASK_APP=Twitoff:APP

flask run
flask shell to run flask inside command line

## Getting information from database inside command line

>>> from Twitoff.models import *
>>> DB.drop_all()
>>> DB.create_all()
>>> u1 = User(name = 'austen', id=89790)
>>> t1 = Tweet(text='adadad', id=890)
>>> u1
<User austen>
>>> t1
<Tweet adadad>
>>> u1.tweets
[]
>>> u1.tweets.append(t1)
>>> u1.tweets
[<Tweet adadad>]
>>> DB.session.add(u1)
>>> DB.session.add(t1)
>>> DB.session.commit()
>>> from Twitoff.models import User
>>> u1 = User.query.filter(User.name == 'austen').first()
>>> u1
<User austen>
>>> u1.tweets
[<Tweet adadad>]
>>> u1.name
'austen'
>>> exit()

## Basilica

flask shell
from TWITOFF.twitter import *
twitter_user = TWITTER.get_user('elonmusk')
tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, mode='extended')
tweets[1].text

tweet_text = tweets[0].text
embedding=BASILICA.embed_sentence(tweet_text,model='twitter')

--------------------------------------------------------------------------------------

>>> from TWITOFF.twitter import *
>>> twitter_user=TWITTER.get_user('elonmusk')
>>> tweets=twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode='extended')
>>> db_user = User(id=twitter_user.id, name=twitter_user.screen_name, newest_tweet_id=tweets[0].id)

>>> for tweet in tweets:
...     embedding=BASILICA.embed_sentence(tweet.full_text,model='twitter')
...     db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:500], embedding=embedding)
...     DB.session.add(db_tweet)
...     db_user.tweets.append(db_tweet)

>>> DB.session.add(db_user)
>>> DB.session.commit()