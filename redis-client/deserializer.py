
class Deserializer:
    
    @classmethod
    def deserialize(cls,response):
        if response[0] == "+":
            return cls.deserialize_simple_string(response)
        elif response[0] == ":":
            return cls.deserialize_integer(response)
        elif response[0] == "$":
            return cls.deserialize_bulk_string(response)
    
    @classmethod
    def deserialize_bulk_string(cls, string):
        if string[:2] == "$-":
            return None  
        else:
            length_end = string.index('\r\n')
            length = int(string[1:length_end])
            data_start = length_end + 2
            data_end = data_start + length
            return string[data_start:data_end]
        
    
    @classmethod
    def deserialize_simple_string(cls,string):
        return string[1:-2]
    
    @classmethod
    def deserialize_integer(cls,string):
        return int(string[1:-2])