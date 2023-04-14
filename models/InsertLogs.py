import json
from pydantic import BaseModel

class LogBody(BaseModel):
    User: str
    Log: str 
    start_time: str
    end_time: str 
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)