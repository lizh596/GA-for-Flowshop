# 学  校：东华大学
# 姓  名：李振浩
# 时  间：2023/10/19 16:24
''' 流水车间实例 --  九个工件 -- 五道工序 -- 不含并行机'''
             # 工件    1    2       3    4     5     6       7     8   9     机器
PT =              [[[3,     7,     9,    6,    3,    13,   11,    2,    9],  # 1     每一个工序的加工时间列表
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],  # 2      行索引：机器序号 列索引：工件序号
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],  # 3
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],  # 4
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],  # 5
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],  # 6
                   ],

                   [[9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9,      5,     9,    4,    8,    3,    4,   5,   15],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],],

                   [[9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [   6,    9,    4,    9,    3,    9,    9,    9,    9],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],],

                   [[9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [3,       3,    9,    4,    9,    2,   6,     5,    3],],

                   [[9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    [6,       2,    5,    8,    9,    3,   14,    6,   11],
                    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
                    ],

               ]

#L = 0
State = 5  # 工序总数
Machine = [[0], [1], [2], [4], [3]]  # 每个工序对应的并行机编号
Job = 9  # 工件总数
# J = {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}  # 以字典的格式表示的加工信息，其中字典的键表示工件的序号，
                                     # 对应键的值表示加工该工件共需多少工序
