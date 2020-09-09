# quickJSON - Documentation
Welcome to a quick overview of quickJSON

## What it is?
quickJSON is a Python library designed for working with JSON files. It wraps around the `JSON` module included in the standard library. quickJSON only leaves access to the basics (extract, get, save, and load JSON files)

## Classes and Functions
quickJSON only includes one class, `JSONManager`, which is used for the management of JSON files.

### JSONManager

#### createKey(self, name, value = None)
Given the name and value, create a key for the JSON file to later save.
If you want to append a dictionary, use `createKeysFromDict()` instead.

#### createKeysFromDict(self, dictionary)
Given a dictionary, append it to the JSON file. For other standard purposes, use `createKey()` instead.

#### loadJSON(self, filename = None)
Given a filename, load a specified JSON file. You **MUST** pass in a filename if you didn't when creating the instance.

#### removeKey(self, name)
Given a key name, remove it from the JSON file

#### saveJSON(self, filename = None, formatJSON = True)
Save a formatted (if specified) JSON file to the specified location.

#### updateKey(self, name, value)
Given a name, modify the value of a certain JSON key
