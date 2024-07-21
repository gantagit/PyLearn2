REST API - Example - POSTMAN (newman Report)

REST is an acronym for Representational State Transfer
Client -> Server(State) with 6 rules/constraints

* Client -> Server
* Roy fielding - HTTP -> SOAP(owned) -> Microsoft -> C#, ASP.net .....#
* Design you API using 6 Constraints
* JSON/XML
* HTTP -> Methods, Headers, Cookies
* Auth ->
* No Envelope like SOAP
* Directly send client -> server via JSON/XML

# 6 constraints
## Uniform interface
## Stateless
## Cacheable
## Client -> Server
## Layered System
## Code on Demand (optional)

* https://scrolltest.com/rest/explained

REST API testing
https://restful-booker.herokuapp.com/apidoc/index.html


Import REST API project into the postman | Collection & Test Cases

# Two ways
1) API Documentation :
    a) CURL request - Command line request to work with the REST API
2) No API documentation :
    a) create a rough level documentation by yourself
    b) Module we have to test
    c) Create a collection based on that

API Documentation
1) CURL Request
2) URL's
3) HTTP methods - GET, POST, PUT, PATCH, DELETE
4) Authorization, Cookie, Token
5) Payload - JSON\XML
6) Response
7) Which status code, How you can verify the response

Example :
1. restful booking project
    a) REST API's, what you can - CRUD Operation 
        C - Create, R - Read \ fetch, U - Update, D - Delete
    b)

Test cases for Create Booking
![Test Cases for Create Booking.png](Test%20Cases%20for%20Create%20Booking.png)

Example of Integration Scenarios
![Integration Scenarios.png](Integration%20Scenarios.png)

Javascript - Postman Automation
Write Postman Testcases in Collection
API Automation framework Request + PyTest + Allure Report

