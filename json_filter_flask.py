import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

events = [
    {
        "categories": ["Green Category"],
        "location": "123-456-789",
        "organizer": "abc123"

    },

    {
        "categories": None,
        "location": "789-456-123",
        "organizer": "hello"
    }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>JSON FLASK Filter Testing</h1>
<p>A prototype API JSON FLASK FILTERING.</p>'''


@app.route('/api/v1/resources/events/all', methods=['GET'])
def api_all():
    return jsonify(events)

@app.route('/api/v1/resources/events', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'organizer' in request.args:
        organizer = str(request.args['organizer'])
        print(organizer)
    else:
        return "Error: No organizer field provided. Please specify organizer."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for event in events:
        if event['organizer'] == organizer:
            results.append(event)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()