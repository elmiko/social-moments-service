import flask
import spacy
import vaderSentiment.vaderSentiment as vader

app = flask.Flask(__name__)
analyzer = vader.SentimentIntensityAnalyzer()
english = spacy.load("en_core_web_sm")


def get_sentiments(text):
    result = english(text)
    sents = [str(sent) for sent in result.sents]
    sentiments = [analyzer.polarity_scores(str(s)) for s in sents]
    return sentiments


@app.route("/", methods=["POST", "GET"])
def index():
    if flask.request.method == "GET":
        return "To access this service send a POST request to this URI with" \
               " the text you want analyzed in the body."
    body = flask.request.data.decode("utf-8")
    sentiments = get_sentiments(body)
    return flask.json.dumps(sentiments)
