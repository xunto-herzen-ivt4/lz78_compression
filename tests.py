import lz78
import string
import random

tests = [
    {
        "message": "abcabcabcabcd",
        "dict_size": 16,
        "result": [
            (0, 'a'),
            (0, 'b'),
            (0, 'c'),
            (1, 'b'),
            (3, 'a'),
            (2, 'c'),
            (4, 'c'),
            (0, 'd'),
        ]
    }
]

# Ordinary
for test in tests:
    result = lz78.compress(test['message'], test['dict_size'])
    print(result)
    assert result == test['result']

    message = lz78.decompress(test['result'], test['dict_size'])
    print(message)
    assert message == test['message']
    print('===========================')


# Test with random
for i in range(0, 1000):
    dict_size = random.randint(2, 20)
    case = "".join(
        random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits
        ) for x in range(random.randint(1, 1000))
    )
    print(case)
    print(dict_size)

    result = lz78.compress(case, dict_size)
    print(result)

    message = lz78.decompress(result, dict_size)
    print(message)

    assert message == case
    print('===========================')