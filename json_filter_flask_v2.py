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
    },
	
	 {
        "categories": ["Blue Category"],
        "location": "789-456-123",
        "organizer": "kalyan"
    },
	
	 {
        "categories": None,
        "location": "789-456-123",
        "organizer": "PS Office Hours"
    },
	
	 {
        "categories": ["Green Category"],
        "location": "123-456-789",
        "organizer": "CE Tools"

    },
	
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
    results = []
    categoryresults = []
    nullcategories = []
    
    if 'organizer' in request.args:
        organizer = str(request.args['organizer'])
        print(organizer)
        for event in events:
            if event['organizer'] == organizer:
                results.append(event)
                            
    elif 'categories' in request.args:
        categories = str(request.args['categories'])
        
        for event in events:
            if not (event['categories']):
                nullcategories.append(event)
            else:
                for item in event['categories']:
                    if categories in item:                    
                        categoryresults.append(event)
    else:
        print('Error! Neither Organiser nor Category provided in Search URL')
  
    if len(categories) == 0:
        catresults = nullcategories
    else:
        catresults = categoryresults

    # Create an empty list for our results

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results



    
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(catresults)
    return jsonify(results)
    

app.run()