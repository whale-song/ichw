import turtle
import time
import tkinter

ways = []
method = -1
result = 0

def data_input():
    global w_length, w_width, t_length, t_width, nodes
    wall_size = list(map(int, input('请输入墙壁的大小（长*宽）:\n').split('*')))
    tile_size = list(map(int, input('请输入板砖的大小（长*宽）:\n').split('*')))
    w_length = wall_size[0]
    w_width = wall_size[1]
    t_length = tile_size[0]
    t_width = tile_size[1]
    nodes = int((w_length * w_width) / (t_length * t_width))
    if (w_length * w_width) % (t_length * t_width) == 0:
        pass 
    else:
        print('铺不满。')
        if input('exit? y/n') == 'y':
            exit()

def data_refresh():
    global wall, ways, mstr, method
    wall = set(range(1, w_length * w_width + 1))
    ways.append([])
    method += 1
    mstr = str(bin(method)[2:]).zfill(nodes)

def horizontal():
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
    tp = []
    m = min(list(wall))
    if w_width - ((m // w_length) - 1) >= t_length and w_length - ((m-1) % w_length) >= t_width:
        try:
            for i in range(t_length*t_width):
                wall.remove(m + i*w_length + i//t_length)
                tp.append(m + i*w_length + i//t_length)
        except KeyError:
            return False
        else:
            ways[-1].append(tuple(tp))
            return True
    else:
        return False

def tile():
    data_refresh()
    for i in mstr:
        if i == '0':
            if horizontal() == False:
                del ways[-1]
                break
        elif i == '1':
            if vertical() == False:
                del ways[-1]
                break

def draw():
    t1 = turtle.turtle
    t1.hideturtle()
    t1.speed(0)
    choice = screen.numinput('choosing the method', 'the method you choose is:', None, minval=1, maxval=len(ways))
    drawing = ways[choice - 1]
    

def main():
    data_input()
    t0 = time.process_time()
    while method < (2 ** nodes - 1):
        tile()
    print(ways, '\n', len(ways))
    t1 = time.process_time()
    print(t1 - t0, 'secs')

if __name__ == '__main__':
    main()
    input()