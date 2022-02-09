from typing import Any
import json

class Object(dict):
    def __init__(self, __data: dict | Any = None, **kwargs):
        if not __data and kwargs:
            __data = kwargs
        
        if not __data:
            __data = {}
        
        self.__data = __data
        
        if isinstance(__data, dict):
            for item in __data:
                if isinstance(__data[item], dict):
                    setattr(self, item, Object(__data[item]))
                
                else:
                    setattr(self, item, __data[item])

    def keys(self) -> list:
        return self.__data.keys()

    def clear(self) -> dict: 
        return self.__data.clear()

    def copy(self) -> 'Object':
        return Object(self.__data.copy())

    def has_key(self, __key: Any) -> bool:
        return __key in self.__data

    def update(self, *args: list, **kwargs: dict) -> 'Object':
        return Object(self.__data.update(*args, **kwargs))

    def values(self) -> list:
        return self.__data.values()

    def items(self) -> list:
        return self.__data.items()

    def to_dict(self) -> dict:
        return self.__data
    
    def to_json(self) -> str:
        return json.dumps(self.__data)

    @staticmethod
    def load(data: str):
        return Object(json.loads(data))

    def __eq__(self, __item) -> bool:
        if isinstance(__item, Object):
            __item = __item.to_dict()

        return self.__data == __item

    def __getitem__(self, __name: str) -> Any:
        try: return Object(getattr(self, __name))
        except AttributeError: return

    def __setattr__(self, __key: str, __value: Any) -> None:
        if __key != '_Object__data':
            self.__data[__key] = __value

        return super().__setattr__(__key, __value)
    
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

    def __delitem__(self, __key):
        try:
            setattr(self, __key, None)
            del self.__data[__key]
        except:
            return
    
    def __repr__(self):
        return repr(self.__data)

    def __len__(self):
        return len(self.__data)