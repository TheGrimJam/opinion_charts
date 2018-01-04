# /usr/bin/!
# Gavin McCormack
from textblob import TextBlob

class sentimentItem:
	def __init__(self, time, text):
		self.date = time
		self.text = "Text of the message"
		self.sentiment = self.retrieve_sentiment(text)

	def retrieve_sentiment(self, text):
		# Textblob sentiment analysis here
		blob = TextBlob(text)
		return blob.polarity
