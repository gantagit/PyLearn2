JSON
- Java Script Object Notation, 
- used for the data transformation from client to server and vice versa
- Key Value Pairs

Demo of JSON
https://jsonpathfinder.com

JSON Data types
1) String
2) number
3) boolean 
4) null
5) array
6) object

# JSON Object Containing JSON Array
**Json Example for JSON Object Containing JSON Object**
    {
        "employee" : {
        "name": "VJ",
        "age": 43,
        "gst": 2016,
        "is_married": true,
        "no of cars" : null,
        "address" : {
            "street 1" : 101,
            "Street 2" : "BBC Studios",
            "city": "London",
            "Country" : "United Kingdom"
            },
        "Phone numbers" : [
            987654321,
            123456789
            ]
        }
    }

# JSON Arrays Containing JSON Object
**Json Example for JSON Array Containing JSON Object**
[
        {
        "name": "VJ",
        "age": 43,
        "gst": 2016,
        "is_married": true,
        "no of cars" : null,
        "address" : {
            "street 1" : 101,
            "Street 2" : "BBC Studios",
            "city": "London",
            "Country" : "United Kingdom"
            },
        "Phone numbers" : [
            987654321,
            123456789
            ]
        },
        {
        "name": "GANTA",
        "age": 43,
        "gst": 2016,
        "is_married": true,
        "no of cars" : null,
        "address" : {
            "street 1" : 101,
            "Street 2" : "BBC Studios",
            "city": "London",
            "Country" : "United Kingdom"
            },
        "Phone numbers" : [
            987654321,
            123456789
            ]
        }
]

# JSON Object Containing JSON Object
**Json Example for JSON Object Containing JSON Array**
{
    "employees" :[
        {
        "name": "VJ",
        "age": 43,
        "gst": 2016,
        "is_married": true,
        "no of cars" : null,
        "address" : {
            "street 1" : 101,
            "Street 2" : "BBC Studios",
            "city": "London",
            "Country" : "United Kingdom"
            },
        "Phone numbers" : [
            987654321,
            123456789
            ]
        },
        {
        "name": "GANTA",
        "age": 43,
        "gst": 2016,
        "is_married": true,
        "no of cars" : null,
        "address" : {
            "street 1" : 101,
            "Street 2" : "BBC Studios",
            "city": "London",
            "Country" : "United Kingdom"
            },
        "Phone numbers" : [
            987654321,
            123456789
            ]
        }
    ]
}

# JSON Pathfinder
https://jsonpathfinder.com
{
  "instructions": [
    "Enter your JSON in the editor.",
    "Select an item to view its path.",
    "Replace 'x' with the name of your variable."
  ]
}

# XML
<?xml version="1.0" encoding="UTF-8" ?>
 <root>
     <employee>
         <name>VJ</name>
         <age>43</age>
         <gst>2016</gst>
         <is_married>true</is_married>
         <no of cars></no of cars>
         <address>
             <street 1>101</street 1>
             <Street 2>BBC Studios</Street 2>
             <city>London</city>
             <Country>United Kingdom</Country>
         </address>
         <Phone numbers>987654321</Phone numbers>
         <Phone numbers>123456789</Phone numbers>
     </employee>
 </root>


# Postman Basics - SOAP
SOAP
simple object access protocol
client -> server - give me the data
SOAP is based on XML
SOAP is a W3C recommendation
more secure
Envelope - information you need to wrap and open and close

# Testing SOAP requests in Postman
https://www.dataaccess.com/webservicesserver/numberconversion.wso?op=NumberToWords

Collection
https://api.postman.com/collections/37107034-341d8be9-9797-4c50-a445-4b72966eff76?access_key=

Test Cases



REST - Example - POSTMAN (newman Report)
Javascript - Postman Automation
API Automation framework Request + PyTest + Allure Report

