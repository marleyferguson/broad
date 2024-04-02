#get request to MBTA api given a string path
def make_api_call(path):
    url = 'https://api-v3.mbta.com/' + path
    response = r.get(url)
    if response.status_code != r.codes.ok:
        raise RuntimeError(response.status_code, response.reason)
    json = response.json()
    return json['data']



#Question 1: sends get request to MBTA API to retrieve the long names of subway-only routes
def get_route_long_names():
    data = make_api_call('routes?filter[type]=0,1')
    long_names =[]
    for route in data:
        long_names.append(route['attributes']['long_name'])
        return long_names
    

