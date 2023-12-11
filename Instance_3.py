# 学  校：东华大学
# 姓  名：李振浩
# 时  间：2023/10/19 16:24
''' 流水车间实例 --  十九个工件 -- 五道工序 -- 含两个并行机 '''
             # 工件    1    2       3    4     5     6       7     8   9     10    11    12    13    14    15    16    17    18    19   机器
PT =              [[[2,       7,    9,    6,    3,    9,    9,    3,    9,    9,    3,    9,    9,    3,    9,    9,    3,    9,    9],  # 1
                    [13,      4,   12,   16,    9,    4,    1,    7,    3,    9,    9,    3,    9,    9,    3,    9,    9,    3,    9],  # 2 每一个工序的加工时间列表
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],  # 3 行索引：机器序号 列索引：工件序号
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],  # 4
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],  # 5
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999]   # 6
                   ],

                   [[9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [6,      15,    6,    3,   18,   13,   19,   13,   19,   13,   3,    9,    3,    9,    3,    9,    3,    9,    3],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999]],

                   [[9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [6,       9,    4,    9,   13,    9,    4,    9,   12,    9,    4,    9,    12,    9,    4,    9,    12,   9,   4],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999]],

                   [[9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [3,      13,    9,    4,    9,    12,   9,    2,    9,    12,    9,    2,    9,    12,    9,    2,    9,    12,   9],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999]],

                   [[9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [16,      2,    5,    8,   14,   13,    3,    9,    5,    9,   16,    2,   15,    8,   14,   14,    8,    3,    8],
                    [6,       5,    10,   4,   12,   11,    5,   19,    9,    4,    6,    5,    4,    4,   14,    3,    3,    9,    5]
                    ]
               ]

#L = 0
State = 5  # 工序总数
Machine = [[0, 1], [2], [3], [4], [5, 6]]  # 每个工序对应的并行机编号
Job = 19  # 工件总数
# J = {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}  # 以字典的格式表示的加工信息，其中字典的键表示工件的序号，
                                     # 对应键的值表示加工该工件共需多少工序

