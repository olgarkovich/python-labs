import unittest
import json
from task_2 import to_json


class MyTestCase(unittest.TestCase):
    def test_bool(self):
        self.assertEqual(to_json(True), json.dumps(True))

    def test_int(self):
        self.assertEqual(to_json(534), json.dumps(534))

    def test_float(self):
        self.assertEqual(to_json(45.21), json.dumps(45.21))

    def test_str(self):
        self.assertEqual(to_json("Weekend"), json.dumps("Weekend"))

    def test_none(self):
        self.assertEqual(to_json(None), json.dumps(None))

    def test_list(self):
        self.assertEqual(to_json([1, 3, 'T', 7, False]), json.dumps([1, 3, 'T', 7, False]))

    def test_tuple(self):
        self.assertEqual(to_json((2, 4, 6, 8, 0)), json.dumps((2, 4, 6, 8, 0)))

    def test_dict(self):
        self.assertEqual(to_json({1: [1, 5, 'Y'], False: None, 'F': (2, "j")}),
                         json.dumps({1: [1, 5, 'Y'], False: None, 'F': (2, "j")}))


if __name__ == '__main__':
    unittest.main()
