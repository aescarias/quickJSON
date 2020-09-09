"""
quickJSON

A basic, simple Python module that interfaces with JSON files.
"""

# Imports
import json

class JSONManager:
    """Manages JSON files"""
    def __init__(self, filename = None):
        self.filename = filename
        
        if self.filename != None:
            self.loadJSON(self.filename)
        else:
            self.rawJSON = {}

    def loadJSON(self, filename = None):
        """Load a specified JSON file"""
        if filename == None:
            filename = self.filename
            
        with open(filename, "r+") as f:
            self.rawJSON = json.load(f)
    
    def createKey(self, name, value = None):
        """Create a key for the JSON file to later save. If you want to append a dictionary, use createKeysFromDict() instead"""
        self.rawJSON.update({name : value})

    def createKeysFromDict(self, dictionary):
        """Appends a Python dictionary to the JSON file"""
        self.rawJSON.update(dictionary)
        
    def updateKey(self, name, value):
        """Update a value of a certain JSON key"""
        self.rawJSON[name] = value
        
    def removeKey(self, name):
        """Remove a key from the JSON file"""
        self.rawJSON.pop(name)
        
    def saveJSON(self, filename = None, formatJSON = True):
        """Save a JSON file to the specified location"""
        if filename == None:
            filename = self.filename
        
        with open(filename, "w+") as f:
            if formatJSON:
                json.dump(self.rawJSON, f, indent = 4)
            else:
                json.dump(self.rawJSON, f)
                
