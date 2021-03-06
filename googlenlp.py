import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

def analyze(text):
	document = types.Document(
	    content=text,
	    type=enums.Document.Type.PLAIN_TEXT)

	# Detects the sentiment of the text
	sentiment = client.analyze_sentiment(document=document).document_sentiment

	return sentiment.score