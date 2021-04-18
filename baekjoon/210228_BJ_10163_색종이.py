import sys
sys.stdin = open("/Users/gibonghong/Downloads/10163_input.txt", "r")

N = int(input())
grid = [[0 for col in range(101)] for row in range(101)]

def calc_area(id:int, x, y, width, height):
    '''
    :param id: 색종이 고유 번호

    :param x: 좌하단 x좌표
    :param y: 좌하단 y좌표
    :param width: 직사각형의 가로 길이
    :param height: 직사각형의 세로 길이

    :return:
    '''

    global grid # 전역변수 설정

    for col in range(y, y+height):
        for row in range(x, x+width):
            grid[100-col][row] = id # 높이는 0부터 시작하니까, 인덱스를 고려해서 100을 빼줌

    # return

for id in range(1, N+1):
    x, y, width, height = map(int, input().split())
    calc_area(id, x, y, width, height)

for id in range(1, N+1):
    cnt = 0
    for i in range(101):
        for j in range(101):
            if grid[i][j] == id:
                cnt += 1
    print(cnt)
