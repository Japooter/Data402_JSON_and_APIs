# Data402_JSON_and_APIs

# JSON
 
What does it stand for?
What is it used for?
What is is written in?
What data types can it store/use?
What is the JSON syntax for:
 
- Name value pairs?
- Objects?
- How to separate data objects from one another?
- JSON arrays (these are like lists in python)?


## JSON answers

JSON stands for JavaScript Object Notation. It allows for easy reading and write for humans and is a text format that is completely language independent. It is therefore great for the concept of data-interchange, to allow data to go from one programming language to another (https://www.json.org/json-en.html). This means JSON can be used in data exchange, typically in web applications. (https://www.spiceworks.com/tech/devops/articles/what-is-json/)

JSON has two main structures that it uses: A collection of name/value pairs (also known as key/value pairs in Python with dictionaries) and an ordered list of values (lists).

    
JSON Data Types include: strings, numbers, objects (JSON object, not Python object), arrays (list), booleans and null. You cannot have functions, dates or undefined as data types in JSON (https://www.w3schools.com/js/js_json_datatypes.asp).

In JSON, name/value pairs are known as objects.

    object:
        { -> whitespace -> string -> whitespace -> : -> value -> (,) -> etc. -> }

    array:
        [ -> value -> (,) -> ]

    value:
        whitespace -> string/number/object/array/true/false/null -> whitespace

    string:
        " -> Any codepoint except " or \ or control characters -> "
        " -> \ -> " / \ / / / b / f / n / r / t / (u -> 4 hex digits) -> " (https://www.json.org/json-en.html)


If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.


# APIs
What are APIs?
How are APIs used and why are they popular?
What are REST APIs? What makes an API Restful?
 
What is HTTP?
Find diagrams that showcase:
 
- HTTP Request Structure
- HTTP Response Structure
 
What are the 5 HTTP verbs?


## API answers

API is an acronym for "Application Programming Interface". In short, APIs are therefore a sort of intermediate point between the communication of two distinct applications. They are easily understood by those developing with the API and also to anyone who might be taking a look at them, as their broad understanding is conveyed through modern variations on API formats. (https://www.mulesoft.com/resources/api/what-is-an-api#:~:text=API%20is%20the%20acronym%20for,to%20talk%20to%20each%20other.)


Modern APIs usually come in the form of HTTP or REST, with the former standing for "HyperText Transfer Protocol" (you are likely familiar with a form of this, being on the internet) and the latter being "REpresentational State Transfer". For a system to be "RESTful", they need to be stateless, clearly showing a divide between clients/customers and the server. They need to be representational, have "URIs" and have the capability of caching too. (https://www.codecademy.com/article/what-is-rest). A diagram of the process of API data transfer, seen in RESTful systems, is seen below.

![image](REST_APIs.webp "Data Transfer Diagram")

In communicating between devices, HTTP APIs often use 5 verbs based on what request needs to be made between the devices in question:

- Create new resources to use in the communication between devices (POST)
- Retrieve a single or list of items to read (GET)
- Update an item (PUT)
- Delete an item (DELETE)
- Modify/patch an item's capabilities, you can use JSON Patch language for this (PATCH)

(https://docs.oracle.com/en/cloud/saas/marketing/eloqua-develop/Developers/GettingStarted/APIRequests/HTTP-verbs.htm)
(https://www.restapitutorial.com/lessons/httpmethods.html)

HTTP APIs are able to communicate via the methods of response and request. They are, in essence, the opposites of each other, but to show in different amounts of detail, included is an image of a HTTP Request (Image from Mozilla, https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages/httpmsg2.png) and a HTTP Response (Image from GeeksForGeeks, https://media.geeksforgeeks.org/wp-content/uploads/20210905094321/StructureOfAHTTPResponse-660x374.png). They are shown in this order below.

![image](HTTP_request.png "HTTP Request Structure")

![image](HTTP_response.png "HTTP Response Structure")
