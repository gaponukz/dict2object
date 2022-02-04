from typing import *
import json

class Object(object):
    def __init__(self, __data: Dict[str, Any] | str = None, **kwargs):
        if not __data and kwargs:
            __data = kwargs

        self.__data = __data
        
        if isinstance(self.__data, dict):
            for item in self.__data:
                if isinstance(self.__data[item], dict):
                    setattr(self, item, Object(self.__data[item]))
                
                else:
                    setattr(self, item, self.__data[item])

    def keys(self) -> List[str]:
        return list(self.__data)

    def to_dict(self) -> dict:
        return self.__data

    @staticmethod
    def load(data: str):
        return Object(json.loads(data))

    def __eq__(self, __item) -> bool:
        if isinstance(__item, Object):
            __item = __item.to_dict()

        return self.__data == __item

    def __getitem__(self, __name: str) -> Any:
        return Object(self.__data.get(__name))
    
    def __setitem__(self, key, value):
        self.__data[key] = value
        setattr(self, key, Object(value))
    
    def __str__(self):
        return str(self.__data)
    
    def __del__(self):
        del self.__data
    
    def __delattr__(self, __name: str) -> None:
        try:
            setattr(self, __name, None)
            del self.__data[__name]
        except:
            return
