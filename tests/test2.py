
# Test that the GET from each of the 3 endpoints works: 
# Write a test where you do a search and see if we have data

import requests

test_data = ["1", "2", "all"]

for i in test_data:
    r = requests.get("http://127.0.0.1:5000/genus/"+i)
    print(i, r.text)

