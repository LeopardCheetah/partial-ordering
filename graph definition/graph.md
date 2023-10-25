

# How to use directed_graph.py

## Example Graph

---

    [0] ← [9] → [8]
     ↑     ↑     ↓
    [7] → [4] ← [3]
           ↑     ↓  
          [1] → [5]

    [2]
     ↑
    [6]


<br></br>

## Inputs

---    

    vertices = 10
    edges = [
        (6, 2),
        (1, 4),
        (1, 5),
        (3, 5),
        (3, 4),
        (4, 9),
        (8, 3),
        (9, 8),
        (9, 0),
        (7, 0),
        (7, 4)
    ]

In this example, use `graph_name = Graph(vertices, edges)` to make this graph object.

<br></br>

### Internal Stuffs

---


    edge_list = edges

    adj_matrix = [
                    (incoming)
        (outgoing)  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    ]

    or without the 0s,
    = [
        [ ,  ,  ,  ,  ,  ,  ,  ,  ,  ],
        [ ,  ,  ,  , 1, 1,  ,  ,  ,  ], 
        [ ,  ,  ,  ,  ,  ,  ,  ,  ,  ],
        [ ,  ,  ,  , 1, 1,  ,  ,  ,  ],
        [ ,  ,  ,  ,  ,  ,  ,  ,  , 1],
        [ ,  ,  ,  ,  ,  ,  ,  ,  ,  ],
        [ ,  , 1,  ,  ,  ,  ,  ,  ,  ],
        [1,  ,  ,  , 1,  ,  ,  ,  ,  ],
        [ ,  ,  , 1,  ,  ,  ,  ,  ,  ],
        [1,  ,  ,  ,  ,  ,  ,  , 1,  ]
    ]

    adj_list_in = [
        [7, 9],
        [],
        [6],
        [8],
        [1, 3, 7],
        [1, 3],
        [],
        [],
        [9],
        [4]
    ]

    adj_list_out = [
        [],
        [4, 5]
        [],
        [4, 5]
        [9],
        [],
        [2],
        [0, 4],
        [3],
        [0, 8]
    ]