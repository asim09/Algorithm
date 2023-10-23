tests_locate_card = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
     'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
               'query': 6},
     'output': 2}
]

tests_count_rotation = [
    {
        'input': {
            'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
        },
        'output': 3
    },
    {
        'input': {
            'nums': [4, 5, 6, 7, 8, 1, 2, 3]
        },
        'output': 5
    },
    {
        'input': {
            'nums': [7, 3, 5]
        },
        'output': 1
    },
    {
        'input': {
            'nums': [3, 5, 7, 8, 9, 10]
        },
        'output': 0
    }
]

tests_binary_count_rotation = [
    {
        'input': {
            'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
        },
        'output': 3
    },
    {
        'input': {
            'nums': [4, 5, 6, 7, 8, 1, 2, 3]
        },
        'output': 5
    },
    {
        'input': {
            'nums': [7, 3, 5]
        },
        'output': 1
    },
    {
        'input': {
            'nums': [3, 5, 7, 8, 9, 10]
        },
        'output': 0
    },
    {
        'input': {
            'nums': [1,2,3,4,5,-1,0]
        },
        'output': 5
    }
]
