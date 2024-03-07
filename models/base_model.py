"""BaseModel of all hbnb models

Is the base class from which all other hbnb models inherit.

Classes:
	BaseModel
"""

class BaseModel:
    """The base class from which all hbnb models inherit

    Variables:
    	id(:str:pub): uuid of class instance when it's created
    	created_at(:datetime:pub): datetime when instance is created
    	updated_at(:datetime:pub): datetime when instance is modified

    Methods:
	__str__(:prv): prints: str rep of class instance
	save(:pub): updates the public instance attribute's 'updated_at' \
		value with the current datetime
	to_dict(:pub): returns a dictionary of keys/vaues of instance
    """
