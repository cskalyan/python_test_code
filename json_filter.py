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

results =[]

for event in events:
    if 'categories' in event:
        print(event)
        results.append(event)

print(results)