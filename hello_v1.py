import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

events = [
    {
        "categories": ["Green Category"],
        "location": "123-456-789",
        "organizer": "abc123",
        "subject": "Cloud Open Forum"
    },

    {
        "categories": None,
        "location": "789-456-123",
        "organizer": "hello",
        "subject": "CE Tools Demo"
    },
	
	 {
        "categories": ["Blue Category"],
        "location": "789-456-123",
        "organizer": "kalyan",
        "subject": "Python Demo"
    },
	
	 {
        "categories": None,
        "location": "789-456-123",
        "organizer": "PS Office Hours",
        "subject": "Micro Service Demo"
    },
	
	 {
        "categories": ["Green Category"],
        "location": "123-456-789",
        "organizer": "CE Tools",
        "subject": "CE3 Demo"

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
    subjectresults = []
    
    
    searchstring = request.args
    
    if 'organizer' in searchstring :
        organizer = str(request.args['organizer'])
        print(organizer)
        for event in events:
            if event['organizer'] == organizer:
                results.append(event)
        response = results
        print(response)
    

    elif 'categories' in searchstring:
        categories = str(request.args['categories'])

        for event in events:
            if not (event['categories']):
                nullcategories.append(event)
            else:
                for item in event['categories']:
                    if categories in item:                    
                        categoryresults.append(event)
                        
        if len(categories) == 0:
            catresults = nullcategories
        else:
            catresults = categoryresults
        response = catresults
    
    elif 'subject' in searchstring:
        subject = str(request.args['subject'])
        print(subject)

        for event in events:
            if event['subject'] == subject:
                subjectresults.append(event)
        response = subjectresults

        if len(subject) == 0:
            subresults = nullcategories
        else:
            subresults = subjectresults
        response = subresults
        #print(response)


    else:
        #print('Error! Neither Organiser nor Category provided in Search URL')
        response = 'Error! Neither Organiser nor Category provided in Search URL'
   
    return jsonify(response)
    #return jsonify(catresults)
 
    

app.run()