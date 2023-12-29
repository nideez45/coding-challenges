

class Serializer:
    
    @classmethod
    def serialize(cls,lst):
        resp = "*{}\r\n".format(len(lst))
        for token in lst:
            resp += cls.serialize_string(token)
        return resp
    
    @classmethod
    def serialize_string(cls,string):
        return "${}\r\n{}\r\n".format(len(string),string)