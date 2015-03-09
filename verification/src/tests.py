TESTS = {
    "Rank_01": [
        {
            "input": ["X.O",
                      "XX.",
                      "XOO"],
            "answer": "X",
            "explanation": [1, [0, 0.5], [3, 0.5]]
        },
        {
            "input": ["OO.",
                      "XOX",
                      "XOX"],
            "answer": "O",
            "explanation": [0, [0, 1.5], [3, 1.5]]
        },
        {
            "input": ["OOX",
                      "XXO",
                      "OXX"],
            "answer": "D",
            "explanation": []
        },
        {
            "input": ["O.X",
                      "XX.",
                      "XOO"],
            "answer": "X",
            "explanation": [1, [3, 0], [0, 3]]
        },
        {
            "input": ["OOO",
                      "XX.",
                      ".XX"],
            "answer": "O",
            "explanation": [0, [0.5, 0], [0.5, 3]]
        },
        {
            "input": ["OXO",
                      "XOX",
                      "OXO"],
            "answer": "O",
            "explanation": [0, [0, 0], [3, 3]]
        },
        {
            "input": ["XOX",
                      "OXO",
                      "XOX"],
            "answer": "X",
            "explanation": [1, [3, 0], [0, 3]]
        },
        {
            "input": ["OXO",
                      "XXO",
                      "XOX"],
            "answer": "D",
            "explanation": []
        },
        {
            "input": [".O.",
                      "XXX",
                      ".O."],
            "answer": "X",
            "explanation": [1, [1.5, 0], [1.5, 3]]
        },
        {
            "input": ['...',
                      'XXX',
                      'OO.'],
            "answer": "X",
            "explanation": [1, [1.5, 0], [1.5, 3]]
        },
        {
            "input": ['OOO',
                      'X.X',
                      '.X.'],
            "answer": "O",
            "explanation": [0, [0.5, 0], [0.5, 3]]
        },
        {
            "input": ['O..',
                      'XOX',
                      '..O'],
            "answer": "O",
            "explanation": [0, [0, 0], [3, 3]]
        },
        {
            "input": ['..O',
                      'XOX',
                      'O..'],
            "answer": "O",
            "explanation": [0, [0, 3], [3, 0]]
        },
        {
            "input": ['.XO',
                      'X.X',
                      'OOO'],
            "answer": "O",
            "explanation": [0, [2.5, 0], [2.5, 3]]
        },
        {
            "input": ['.XO',
                      'X.X',
                      'O.O'],
            "answer": "D",
            "explanation": []
        },
        {
            "input": [".OX",
                      ".XX",
                      ".OO"],
            "answer": "D",
            "explanation": []
        },
        {
            "input": ["...",
                      ".X.",
                      "..."],
            "answer": "D",
            "explanation": []
        },
        {
            "input": [".O.",
                      ".X.",
                      "..."],
            "answer": "D",
            "explanation": []
        },
        {
            "input": [".O.",
                      "...",
                      "..."],
            "answer": "D",
            "explanation": []
        },
        {
            "input": [".OX",
                      "..X",
                      ".OX"],
            "answer": "X",
            "explanation": [1, [0, 2.5], [3, 2.5]]
        },
    ],
    "Rank_02": [
        {
            "input": [".OX",
                      ".OX",
                      ".OX"],
            "answer": "D",
            "explanation": [
                [1, [0, 2.5], [3, 2.5]],
                [0, [0, 1.5], [3, 1.5]]]
        },
        {
            "input": ['.XO',
                      'XXX',
                      'OOO'],
            "answer": "D",
            "explanation": [
                [0, [2.5, 0], [2.5, 3]],
                [1, [1.5, 0], [1.5, 3]]],

        },
        {
            "input": ['XXX',
                      'X.O',
                      'OOO'],
            "answer": "D",
            "explanation": [
                [0, [2.5, 0], [2.5, 3]],
                [1, [0.5, 0], [0.5, 3]]
            ],

        },
    ],
    "Rank_03": [
        {
            "input": ['XOO.',
                      '.X.O',
                      'X.OO',
                      'XXOX'],
            "answer": "D",
            "explanation": [
            ],
        },
        {
            "input": ['XOO.',
                      '.X.O',
                      'XXOO',
                      'XXOX'],
            "answer": "X",
            "explanation": [
                [1, [1, 1.5], [4, 1.5]]
            ],
        },
        {
            "input": ['XOO.',
                      '.XOO',
                      'XXOO',
                      'XXOX'],
            "answer": "D",
            "explanation": [
                [1, [1, 1.5], [4, 1.5]],
                [0, [0, 2.5], [4, 2.5]],
            ],
        },
        {
            "input": ['XOO.',
                      '.XOO',
                      'XXOO',
                      'XOOX'],
            "answer": "D",
            "explanation": [
                [0, [1, 4], [4, 1]],
            ],
        },

    ]
}
