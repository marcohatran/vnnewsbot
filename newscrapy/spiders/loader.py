import json

class JsonLoader:
    """Load setting from json file
    
    
    """
    def __init__(filename):
        with open(filename) as f:
            data = json.load(f)
            
        return data