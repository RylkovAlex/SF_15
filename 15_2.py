import os


def isUrl(text):
    return True if text[:7] == 'http://' or text[:8] == 'https://' else False


validation_schema = {
    'timestamp': lambda value: type(value) == int,
    'referer': lambda value: isUrl(value),
    'location': lambda value: isUrl(value),
    'remoteHost': lambda value: type(value) == str,
    'partyId': lambda value: type(value) == str,
    'sessionId': lambda value: type(value) == str,
    'pageViewId': lambda value: type(value) == str,
    'eventType': lambda value: value in ['itemBuyEvent', 'itemViewEvent'],
    'item_id': lambda value: type(value) == str,
    'item_price': lambda value: type(value) == int,
    'basket_price': lambda value: type(value) == int,
    'item_url': lambda value: isUrl(value),
    'basket_price': lambda value: type(value) == str,
    'detectedDuplicate': lambda value: type(value) == bool,
    'detectedCorruption': lambda value: type(value) == bool,
    'firstInSession': lambda value: type(value) == bool,
    'userAgentName': lambda value: type(value) == str,
}


def get_Errors(dict, validation_schema):
    errors = []
    if (len(dict.keys()) > len(validation_schema.keys())):
        errors.append('JSON содержит лишние поля')
    for key in validation_schema.keys():
        if not key in dict:
            errors.append(f'Отсутствует поле {key}')
    for key, value in dict.items():
        if not validation_schema[key](value):
            errors.append(f'Значение поля {key} не валидно')
    return errors


def test_json(file_path):
    import json

    with open(file_path, 'r', encoding='utf-8') as file:
        responses = json.loads(file.read())
        result = {}
        for response in responses:
            result[json.dumps(response, indent=4)] = get_Errors(response, validation_schema)
        if not any([errors for errors in result.values()]):
            print('PASS')
        else:
            for json, errors in result.items():
                if errors:
                    print(f'FAILD for JSON:\n{json}\nERRORS:\n{", ".join(errors)}')


test_json(os.path.join(os.getcwd(), 'example.json'))
