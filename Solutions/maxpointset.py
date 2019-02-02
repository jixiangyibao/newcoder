import sys

if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    sorted_points =sorted(points,key=lambda x:x[0],reverse=True)
    del points
    ret_set = []
    tmp_y = sorted_points[0][1]
    ret_set.append(sorted_points[0])
    for i in range(1, n):
        if tmp_y < sorted_points[i][1]:
            tmp_y = sorted_points[i][1]
            ret_set.append(sorted_points[i])
    ret_num = len(ret_set)
    for i in range(ret_num):
        print("%d %d"%(ret_set[ret_num - i - 1][0],ret_set[ret_num - i - 1][1]))

