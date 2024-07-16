API Testing Notes - PART 2

API - 
    Application programming interface
    Communication interface
    Online(with http) and Offline (without http)

Public APIs
Private APIs

List of APIs
    https://github.com/public-apis/public-apis
    https://apilist.fun

Request
    Client -> Request -> Server
    Methods
        GET, POST, PUT, PATCH, DELETE
    URL + Params(QP or PP) + Headers + Authorization +   Body/Params/ Data

Response
    Server -> Client
    Response Status Code
    Response Data
    Headers
    Time (Verify)

Web Service -
    API over http, to interact over two applications

Types 
    SOAP
        XML (RPC)
    REST
        JSON - GET,POST, PUT, PATCH, DELETE


# What is Test in APIs
    Checking the Response messages, Content and Structure
    Verify Data accuracy and consistency
    Validate Response Status Code and headers
    Response times
    Ensuring proper error handling and security measures
    **Validating the KEYS with Min and Max range of APIS (Example : maximum and minimum length)**
    Have a test case to do XML, JSON Schema validation
    Keys Verification, If we JSON, XML, APIS, We should verify it's all the Keys are coming
    verify that how the API error codes are handled

# Why we should perform API Testing
    ** Developers make mistake and create Buggy APIs**
    Cost Effective
    Early Identification of Bugs
    Easy to Execute or Business early


# Common Bugs
    Incorect Resoonse Status
    Incroect Paramters handling
    Incorrect Response Data
    Incosistent Data handling
    Authentication issues, header issues
    functional issues
    performance issues
    security issues

# HTTP Methods
    GET - Retreve data of a record
    POST - Create a record 
    PUT - Update the full data of a record
    PATCH - Update the partial data of a record
    DELETE - Delete a record 
    DELETE - we can delete all the records but it depends on the server if it is handled in the server










    


