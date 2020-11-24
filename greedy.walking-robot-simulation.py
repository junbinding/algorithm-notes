from typing import List


class Solution:
    """
    874. 模拟行走机器人
    https://leetcode-cn.com/problems/walking-robot-simulation/description/
    机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
        -2：向左转 90 度
        -1：向右转 90 度
        1 <= x <= 9：向前移动 x 个单位长度
    在网格上有一些格子被视为障碍物。
    第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
    机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
    返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。
    """

    def robotSim(self, commands, obstacles):
        # 向北 0,1 向南 0,-1
        dx = [0, 1, 0, -1]
        # 向东 1,0，向西 -1, 0
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            # 左转
            if cmd == -2:
                di = (di - 1) % 4
            # 右转，则改变纵坐标
            elif cmd == -1:  # right
                di = (di + 1) % 4
            else:
                # 遍历本次步数
                for k in range(cmd):
                    # 判断当前走到的位数是否不在障碍物中
                    if (x + dx[di], y + dy[di]) not in obstacleSet:
                        # 向前移动
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x * x + y * y)

        return ans


so = Solution()
print(so.robotSim([4, -1, 3], []))
print(so.robotSim([4, -1, 4, -2, 4], [[2, 4]]))

