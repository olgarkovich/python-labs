import json


def to_json(obj):
    if isinstance(obj, bool):
        if obj:
            return "true"
        else:
            return "false"

    if isinstance(obj, int) or isinstance(obj, float):
        obj = str(obj)
        return obj

    if isinstance(obj, str):
        return '"{}"'.format(obj)

    if obj is None:
        return "null"

    if isinstance(obj, dict):
        result = "{"
        for key, value in obj.items():
            if isinstance(key, str):
                result += '"{}":'.format(key)
            if isinstance(key, (int, float, bool)) or key is None:
                result += '"{}":'.format(to_json(key))

            if isinstance(value, (int, float, str, list, tuple, bool)) or value is None:
                result += ' {}'.format(to_json(value));
            result += ", "
        result = result[:-2] + "}"
        return result

    if isinstance(obj, list) or isinstance(obj, tuple):
        result = "["
        for value in obj:
            if isinstance(value, (str, int, float, bool)):
                result += to_json(value)
            elif value is None:
                result += to_json(value)
            result += ", "
        result = result[:-2] + "]"
        return result

    print("Error, value does not match possible")

# a = {1: 'R', '8': True, None: None, 5.6: "srsrsrsr", False: 4}
# print(to_json(a))
# b = {1: 'R', '8': True, None: None, 5.6: "srsrsrsr", False: 4}
# print(json.dumps(b))
