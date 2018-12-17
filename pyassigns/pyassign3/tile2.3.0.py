#!/usr/bin/env python3

"""
tile.py: count words from an Internet file.

__author__ = "WhaleSong"
__pkuid__  = "1800011751"
__email__  = "whalesong@pku.edu.cn"
__version__ = 2.3.0

更新日志：
2.3.0
在穷举中增添了规避算法，对出错节点进行规避，从而避免对错误结果的多次重复运算。
"""

# 本版本为铺砖的穷举版本，旨在通过生成相应长度的二进制数覆盖所有可能的铺法。

import turtle
from time import process_time, sleep

ways = []
method = -1
result = 0
p = False

def data_input():
    '''
    collect the data that the calculation needed from user input.
    w_length: length of the wall
    w_width: width of the wall
    t_length: length of the tiles
    t_width: width of the tiles
    nodes: total nodes(number of the tiles)
    maximum: the maximum number of the methods
    '''
    global w_length, w_width, t_length, t_width, nodes, maximum
    w_length, w_width, t_length, t_width = map(int, input(
        '请依次输入墙长、墙宽、砖长、砖宽（以空格隔开）：\n'
        ).split())
    nodes = int((w_length * w_width) / (t_length * t_width))
    maximum = 2 ** nodes - 1
    if (w_length * w_width) % (t_length * t_width) == 0:
        pass 
    else:
        print('铺不满。\n exit in 10 seconds...')
        sleep(10)
        exit()

def data_refresh(position):
    '''
    refresh the current position of the wall and other constants.
    p: position of the avoiding arithmetic.
    mstr: the method to tile.(binary number)(type: string)
    method: the method to tile.(decimalism number)
    '''
    global p, wall, ways, mstr, method
    wall = set(range(1, w_length * w_width + 1))
    if position == False:
        method += 1
        mstr = str(bin(method)[2:]).zfill(nodes)
    else:
        p = False
    ways.append([])

def tile_squares():
    '''
    tile when tiles are squares(t_length = t_width)
    '''
    if w_length % t_length != 0 or w_width % t_length != 0:
        print('铺不满。\n exit in 10 seconds...')
        sleep(10)
        exit()
    else:
        data_refresh(False)
        for i in range(nodes):
            horizontal()

def horizontal():
    '''
    try to tile in horizontal direction, if not able to complete, return False.
    tp: the squares included in the tiles
    m: the minimum number of squares remaining in the wall
    '''
    tp = []
    m = min(list(wall))
    if w_length - ((m-1) % w_length) >= t_length and w_width - ((m // w_length) - 1) >= t_width:
        try:
            for i in range(t_width*t_length):
                wall.remove(m + i%t_length + i//t_length * w_length)
                tp.append(m + i%t_length + i//t_length * w_length)
        except KeyError:
            return False
        else:
            ways[-1].append(tuple(tp))
            return True
    else:
        return False

def vertical():
    '''
    try to tile in vertical direction, if not able to complete, return False.
    tp: the squares included in the tiles
    m: the minimum number of squares remaining in the wall
    '''
    tp = []
    m = min(list(wall))
    if w_width - ((m // w_length) - 1) >= t_length and w_length - ((m-1) % w_length) >= t_width:
        try:
            for i in range(t_length*t_width):
                wall.remove(m + (i//t_width)*w_length + i%t_width)
                tp.append(m + (i//t_width)*w_length + i%t_width)
        except KeyError:
            return False
        else:
            ways[-1].append(tuple(tp))
            return True
    else:
        return False

def tile():
    '''
    The main function to tile. If any tiling function returned False, record the node and run avoiding arithmetric.
    '''
    global p, mstr, method, nodes
    data_refresh(p)
    for i in range(nodes):
        if mstr[i] == '0':
            if horizontal() == False:
                del ways[-1]
                method += int(str(10 ** (nodes-i-1)), 2)
                mstr = str(bin(method)[2:]).zfill(nodes)
                p = True
                break
        elif mstr[i] == '1':
            if vertical() == False:
                del ways[-1]
                method += int(str(10 ** (nodes-i-1)), 2)
                mstr = str(bin(method)[2:]).zfill(nodes)
                p = True
                break

def draw_brick(turtle, direction, length, width):
    '''
    draw a tile in horizontal or vertical direction.
    turtle: the name of the running turtle.
    direction: the direction to draw the tile.
    length: length of the tile.
    width: width of the tile.
    '''
    if direction == 'horizontal':
        for i in range(2):
            turtle.fd(length*20)
            turtle.lt(90)
            turtle.fd(width*20)
            turtle.lt(90)
    else:
        for i in range(2):
            turtle.fd(width*20)
            turtle.lt(90)
            turtle.fd(length*20)
            turtle.lt(90)

def draw():
    '''
    use the turtle to draw the wall and tiles.
    choice: the method of tiling that user selected.
    brick: the very tile that is being drawn.
    t1: the drawing turtle.
    t2: the writing turtle(currently not used).
    '''
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t1.speed(0)
    t2.hideturtle()
    t2.speed(0)
    choice = int(
        turtle.numinput(
            'choosing the method', 
            'the method you choose is:', 
            None, 
            minval=1, 
            maxval=len(ways)
            )
        )
    draw_method = ways[choice - 1]
    for i in draw_method:
        brick = list(i)
        t1.penup()
        t1.goto(
            -10*w_length + ((brick[0]-1)%w_length)*20,
            -10*w_width + ((brick[0]-1)//w_length)*20
            )
        t1.pendown()
        if (max(brick) - min(brick)) // w_length == (t_width - 1):
            draw_brick(t1, 'horizontal', t_length, t_width)
        else:
            draw_brick(t1, 'vertical', t_length, t_width)
    turtle.done()


def main(): 
    data_input()    #输入数据
    t0 = process_time()     #记录开始时间
    if t_length == t_width:
        tile_squares()      #遇正方形砖运行简化算法
    else:
        while method <= (maximum):      #设置运行次数上限
            tile()
    t1 = process_time()     #记录结束时间
    if ways == []:      #若为空结果则退出
        print('铺不满。\n exit in 10 seconds...')
        sleep(10)
        exit()
    for i in range(len(ways)):
        print(i+1, ways[i])     #输出各铺法
    print(
        '\n', '-' * 30, '\n',
        '{} methods in total, using {} seconds.\n'.format(
        len(ways), t1-t0
        ),
        '-'*30
    )
    if input('choose one to draw? y/n\n') == 'y':
        draw()

if __name__ == '__main__':
    main()
