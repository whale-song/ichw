import turtle
from time import process_time

ways = []
method = -1
result = 0
p = False

def data_input():
    global w_length, w_width, t_length, t_width, nodes, maximum
    w_length, w_width, t_length, t_width = map(int, input(
        '请依次输入墙长、墙宽、砖长、砖宽（以空格隔开）：\n'
        ).split())
    nodes = int((w_length * w_width) / (t_length * t_width))
    maximum = 2 ** nodes - 1
    if (w_length * w_width) % (t_length * t_width) == 0:
        pass 
    else:
        print('铺不满。')
        if input('exit? y/n') == 'y':
            exit()

def data_refresh(position):
    global p, wall, ways, mstr, method
    wall = set(range(1, w_length * w_width + 1))
    if position == False:
        method += 1
        mstr = str(bin(method)[2:]).zfill(nodes)
    else:
        p = False
    ways.append([])

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

def draw():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    for i in [t1, t2]:
        i.hideturtle()
        i.speed(0)
        i.penup()
    choice = screen.numinput(
        'choosing the method', 
        'the method you choose is:', 
        None, 
        minval=1, 
        maxval=len(ways)
        )
    draw_method = ways[choice - 1]
    t1.goto(-10*t_length,-10*t_width)
    t1.pendown()
    for i in draw_method:
        pass

def main():
    global maximum
    data_input()
    t0 = process_time()
    while method <= (maximum):
        tile()
    t1 = process_time()
    print(ways, '\n', len(ways))
    print(t1 - t0, 'secs')
    if input('choose one to draw? y/n\n') == 'y':
        draw()

if __name__ == '__main__':
    main()
    input()