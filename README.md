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

JSON notes:
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
