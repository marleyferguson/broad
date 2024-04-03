import requests as r
import sys

#defines a subway route with an id, long_name, and stops
class Route():
    def __init__(self, r_id, long_name):
        self.r_id = r_id
        self.long_name=long_name
        self.stops = []
       
    def Route(self, r_id, long_name, stops):
        self.r_id = r_id
        self.long_name=long_name
        self.stops = stops
    def get_id():
        return self.r_id
    def get_long_name():
        return self.long_name
    def get_stops():
        return self.stops
    def add_stop(self, stop):
        self.stops.append(stop)




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

def get_route_ids():
    data = make_api_call('routes?filter[type]=0,1')
    ids = []
    for route in data:
        n = route['id']
        ids.append(str(n)) 

    return ids
    
#initializes all the routes 
def create_routes():
    ids = get_route_ids()
    long_names = get_route_long_names()
    route_l =[]
    for r_id, long_name in zip(ids, long_names):
        r = Route(r_id,long_name)
        route_l.append(r)
    return route_l

#adds stops to all the routes
def add_stops(routes):
    for route in routes:    
        r_id = route.r_id
        path = 'stops?filter[route]={}'.format(r_id)
        data = make_api_call(path)
        for stop in data:
            val = stop['attributes']['name']
            route.add_stop(val)

    return routes

    
#Question 2:
#2.1 returns the route with the most stops and the number of stops
def get_route_max_stops(routes):
    max_stops = 0
    long_name = ''
    for route in routes:
        num_stops = len(route.stops)
        if num_stops > max_stops:
            max_stops = num_stops
            long_name= route.long_name
    return long_name, max_stops

#2.2 returns the route with the least stops and the number of stops
def get_route_min_stops(routes):
    min_stops = 10000
    long_name = ''
    for route in routes:
        num_stops = len(route.stops)
        if num_stops < min_stops:
            min_stops = num_stops
            long_name= route.long_name
    return long_name, min_stops

#2.3 
#returns each stop mapped to the routes it connects
def stop_to_route(routes):
    stop_to_route = {}
    for route in routes:
        for stop in route.stops:
            if stop not in stop_to_route:
                add = []
            else: 
                add = stop_to_route[stop]
            add.append(route)
            stop_to_route[stop] =add
    return stop_to_route

#returns stops that connect 2 or more routes with connecting routes mapped  
def shared_stops(routes):
    stops_routes = stop_to_route(routes)
    shared_stops ={}       
    for stop in stops_routes:
        if len(stops_routes[stop]) >1:
            val = list(map(lambda x:x.long_name,stops_routes[stop] ))            
            shared_stops[stop] = val
    return shared_stops

#Question 3: finds the route in betweenthe two given stops 
def find_route(stop1,stop2,routes):
    
    
    #maps each stop to avail routes
    stops_w_routes = stop_to_route(routes)
    
    #routes stop2 is on
    stop2_routes = stops_w_routes[stop2]
    
    #stops with multiple routes, mapped to their routes
    nodes = shared_stops(routes)

    visited_routes =[]
    Q =[]
    Q.append((stop1,''))
    while len(Q) !=0:
        n,rt = Q.pop(0)
        
        #routes accessible by this node n
        routes_to_check= stops_w_routes[n]
        
        #check each route for stop2 if they havent been checked yet
        for current_route in routes_to_check:
            if current_route.long_name not in visited_routes:
                visited_routes.append(current_route.long_name )
                if rt != '':
                    
                    rt = rt + ', '+ current_route.long_name
                else:
                    rt = current_route.long_name
                
                #if find it, return it
                if stop2 in current_route.stops:
                    return rt
                #dont find it, mark route as visited
                else:
                    visited_routes.append(current_route.long_name)
                #check each route for the stops that have access to other routes
                for s in current_route.stops:
                    if s in nodes:
                        Q.append((s,rt))
            
                
def main():
    if len(sys.argv) < 2:
            print("Usage: python my_script.py [function_name]")
            return

        function_name = sys.argv[1]
        if function_name == "question1":
            get_route_long_names()
        
        else:
            print("Unknown function:", function_name)


