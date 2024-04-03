Problem description
Boston's transportation system, the MBTA (https://mbta.com/), has a website with APIs https://apiv3.mbta.com/docs/swagger/index.html.
You will not need an API key, but you might get rate-limited without one.
The MBTA's documentation https://api-v3.mbta.com/docs/swagger/index.html 

Question 1
Write a program that retrieves data representing all, what we'll call "subway" routes: "Light Rail" (type 0) and
“Heavy Rail” (type 1). The program should list their “long names” on the console.
Partial example of long name output: Red Line, Blue Line, Orange Line...
There are two ways to filter results for subway-only routes. Think about the two options below and choose:
1. Download all results from https://api-v3.mbta.com/routes then filter locally
2. Rely on the server API (i.e., https://api-v3.mbta.com/routes?filter[type]=0,1) to filter before results
are received
Please document your decision and your reasons for it.

Question 2
Extend your program so it displays the following additional information.
1. The name of the subway route with the most stops as well as a count of its stops.
2. The name of the subway route with the fewest stops as well as a count of its stops.
3. A list of the stops that connect two or more subway routes along with the relevant route names for
each of those stops.

Question 3
Extend your program again such that the user can provide any two stops on the subway routes you listed for
question 1.
List a rail route you could travel to get from one stop to the other. We will not evaluate your solution based
upon the efficiency or cleverness of your route-finding solution. Pick a simple solution that answers the
question. We will want you to understand and be able to explain how your algorithm performs.


