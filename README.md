# quickJSON
quickJSON is a Python library designed for interfacing with JSON files. It is a simple module that makes it easier for users to extract, save, and load JSON data.

## Example

**Code**

    from quickJSON import JSONManager
    a = JSONManager()  
    a.createKey("data", {"name" : "John", "age"  : 10})
    a.saveJSON("a.json")

**JSON File**

    {
        "data": {
            "name": "John",
            "age": 10
        }
    }
