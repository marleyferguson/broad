# Testing

## Command line Testing
#### Different inputs were tested on the command line to make sure it functions properly. For example, 'question4' is an invalid input and alerts the user that the question is invalid. 
#### Additionally, failing to add two valid mbta stops for question3 alerts the user to do so. 

## Question 1 and 2 Testing
#### Question 1 and 2 were tested by checking that the output is valid according to the MBTA map of stops and routes. 

## Question 3 Testing
#### Question 3 was tested by inputing different pairs of stops on the MBTA and determining accuracy by checking the map. For example, 'Park Street' and 'Alewife' return 'Red Line'. 
#### There is a failure to optimize the route in the program. For example, 'Alewife' 'Northeastern University' returns 'Red Line, Greenline B, Greenline C, Greenline D, Greenline E'.
#### If it were optimized correctly, it would return 'Redline, Greenline E'. While the original path is not incorrect, it is not fully optimized to the shortest route. 
#### If the stops are inputed incorrectly, for example 'Northeastern' instead of 'Northeastern University', the program alerts the user of this mistake. 

