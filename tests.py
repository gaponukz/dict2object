import unittest

from dict2object.dict2object import Object

class TestObjectMethods(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Object(), {})
        self.assertEqual(Object(a=1), {"a": 1})
        self.assertEqual(Object(a={"b": 1}), {"a": {"b": 1}})
        self.assertEqual(Object({"a": {"b": {"c": 1}}}), {"a": {"b": {"c": 1}}})
    
    def test_atributes(self):
        self.assertEqual(Object(a="value").a, "value")
        self.assertEqual(Object(a={"b": "value"}).a.b, "value")
        self.assertEqual(Object({"a": {"b": {"c": 1}}}), {"a": {"b": {"c": 1}}})

        item = Object()
        item.a = "value"

        self.assertEqual(item.a, "value")
        self.assertEqual(item.b, {})
    
    def test_json_methods(self):
        self.assertEqual(Object.load('{"a": "value"}'), {"a": "value"})
        self.assertEqual(Object.load('{"a": {"b": "value"}}'), {"a": {"b": "value"}})
    
    def test_methods(self):
        obj1 = Object({"a": 1,"b": 1,"c": 1})
        obj2 = obj1.copy()

        self.assertEqual(obj1, obj2)

        self.assertEqual(obj1, Object.fromkeys(['a', 'b', 'c'], 1))
        self.assertEqual(obj1.filter(lambda x: x != 1), {})
        self.assertEqual(list(obj2), ['a', 'b', 'c'])
        self.assertEqual(obj2.to_dict(), {"a": 1,"b": 1,"c": 1})
        self.assertTrue(obj2.has_key('a'))
    
    def test_operators(self):
        obj1 = Object({"a": 1,"b": 1,"c": 1})
        obj2 = obj1.copy()

        self.assertTrue(obj1 == obj2)
        self.assertTrue(obj1 == {"a": 1,"b": 1,"c": 1})

        obj1.a = "value"
        self.assertEqual(obj1.a, "value")
        obj1 += {"d": 1}

        self.assertEqual(obj1.d, 1)
        self.assertTrue("d" in obj1)
        self.assertTrue(obj1)
        self.assertTrue(not Object())

        self.assertEqual(len(obj1), 4)
        self.assertEqual(obj1.length, 4)

if __name__ == '__main__':
    unittest.main()