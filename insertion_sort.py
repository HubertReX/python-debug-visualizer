"""Python demo for sorting using VS Code Debug Visualizer."""


import json


def serialize(arr):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": {"grid": True},
        "rows": [
            {
                "columns": [
                    {"content": str(value), "tag": str(value)} for value in arr
                ],
            }
        ],
    }
    return json.dumps(formatted)


def serialize_dict(dct):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": {"grid": True},
        "rows": []
        #     {
        #         "columns": [{"content": str(key), "tag": str(key)} for key in dct],
        #     },
        #     {
        #         "columns": [{"content": str(value), "tag": str(value)} for value in dct.values()],
        #     }

        # ],
    }
    for key in dct:
        formatted["rows"].append(
            {
                "columns": [
                    {"content": key,           "tag": key},
                    {"content": str(dct[key]), "tag": str(dct[key])}
                ]
            }
        )

    return json.dumps(formatted)


arr = [6, 9, 3, 12, 1, 11, 5, 13, 8, 14, 2, 4, 10, 0, 7]
dct = {
    "a": 123,
    "b": 456,
    "c": 789
}

# Put serialized into the Debug Visualizer console
serialized = serialize(arr)
serialized_dict = serialize_dict(dct)
# Set a breakpoint on the line below and go through the code in debug mode to
# watch it update
for target_idx in range(1, len(arr)):
    target_value = arr[target_idx]
    compare_idx = target_idx - 1

    while compare_idx >= 0 and arr[compare_idx] > target_value:
        arr[compare_idx + 1] = arr[compare_idx]
        serialized = serialize(arr)
        compare_idx -= 1

    arr[compare_idx + 1] = target_value
    serialized = serialize(arr)

assert arr == sorted(arr)
