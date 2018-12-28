# coding:utf-8
import os
import runCFile
f = open("chuanxing.c", "r")
f_  = open("bing.c" , "w")
lines = f.readlines()

# N = 1

row = [17]
operater = [0] # 0-reduction,1-critical,2-atomic
head = r'#include "omp.h"'
def openmp_set(N):
    return "omp_set_num_threads(" + str(N) + ");"
openmp_dad = "#pragma omp parallel for"
def openmp_red(ad, op):
    return "#pragma omp parallel for reduction(" + op + ":" + ad + ")"
openmp_criti = "#pragma omp critical"
openmp_ato = "#pragma omp atomic"
i = 0
flag = 0
clock = r"#include <time.h>"
clock_start = "clock_t start = clock();"
clock_stop = "clock_t end = clock();"
clock_print = r'printf("Time : %lf ms\n", (double)(end - start));'
#print(openmp)
forList = []
row_for = 0
row_for_end = 0
def isOk(num):
    left = 0
    right = 0
    for n in range(num, len(lines)):
        if lines[n].find('{') != -1:
            left += 1
        if lines[n].find('}') != -1:
            right += 1
        forList.append(lines[n])
        if left == right and left != 0:
            break
    for l in forList:
        l = l.strip()
        #print(l)
    row_for_end = n
    return True

def add_reduction(r, flag, i, ad, op,N):
    s = lines[r]
    if s.find("+=") != -1:
        loc = s.find("+=")
        ad = s[:loc].strip()
        op = '+'
    elif s.find("*=") != -1:
        loc = s.find("*=")
        ad = s[:loc]
        op = '*'
    elif s.find("/=") != -1:
        loc = s.find("/=")
        ad = s[:loc]
        op = '/'
    elif s.find("-=") != -1:
        loc = s.find("-=")
        ad = s[:loc]
        op = '-'
    lines.insert(row_for, openmp_set(N) + '\n')
    lines.insert(row_for+1, openmp_red(ad, op)+'\n')
    i += 1
    flag += 2

    return i, flag, ad, op

def add_dad(r, row_for, row_for_end,N):
    lines.insert(row_for, openmp_set(N))
    lines.insert(row_for+1, openmp_dad + '\n')
    lines.insert(row_for + 2, '{' + '\n')
    row_for += 3
    row_for_end += 3
    lines.insert(row_for_end + 1, '}' + '\n')
    return row_for, row_for_end
def add_critical(r):
    r = r + 4
    lines.insert(r, openmp_criti + '\n')

def add_atomic(r):
    r = r + 4
    lines.insert(r, openmp_ato + '\n')
def WEN(filePath, row, operater, N):

    op = "+"
    ad = "sum"

    head = r'#include "omp.h"'

    openmp_dad = "#pragma omp parallel for"

    openmp_criti = "#pragma omp critical"
    openmp_ato = "#pragma omp atomic"
    i = 0
    flag = 0
    clock = r"#include <time.h>"
    clock_start = "clock_t start = clock();"
    clock_stop = "clock_t end = clock();"
    clock_print = r'printf("Time : %lf ms\n", (double)(end - start));'
    # print(openmp)
    forList = []
    row_for = 0
    row_for_end = 0

    f = open(filePath, "r")
    f_ = open("bing.c", "w")
    lines = f.readlines()
    flag = 0
    for r in range(len(lines)+30):
        #print(lines[r])
        # print(lines[r])
        # print(flag)
        if r == len(lines):
            break
        if flag != 0:
            flag -= 1
            continue
        if str(lines[r]).find("main") != -1:
            lines.insert(r + 2, clock_start + '\n')
        if str(lines[r]).find("return") != -1:
            lines.insert(r, clock_stop + '\n')
            lines.insert(r + 1, clock_print + '\n')
            flag += 2
            #print("re")

        if lines[r].find('for') != -1:
            left = 0
            right = 0
            for n in range(r, len(lines)):
                if lines[n].find('{') != -1:
                    left += 1
                if lines[n].find('}') != -1:
                    right += 1
                forList.append(lines[n])
                if left == right and left != 0:
                    break
            for l in forList:
                l = l.strip()
                # print(l)
            row_for_end = n

            row_for = r
        if i == len(row):
            i = i - 1
        if r+1 == row[i]:
            if operater[i] == 0:
                s = lines[r+1]
                if s.find("+=") != -1:
                    print("w")
                    loc = s.find("+=")
                    ad = s[:loc].strip()
                    op = '+'
                elif s.find("*=") != -1:
                    loc = s.find("*=")
                    ad = s[:loc]
                    op = '*'
                elif s.find("/=") != -1:
                    loc = s.find("/=")
                    ad = s[:loc]
                    op = '/'
                elif s.find("-=") != -1:
                    loc = s.find("-=")
                    ad = s[:loc]
                    op = '-'
                lines.insert(row_for, openmp_set(N) + '\n')
                lines.insert(row_for + 1, openmp_red(ad, op) + '\n')
                i += 1
                flag += 2

                row_for += 2
                row_for_end += 2

            elif operater[i] == 1:
                lines.insert(row_for, openmp_set(N) + '\n')
                lines.insert(row_for + 1, openmp_dad + '\n')
                row_for += 2
                row_for_end += 2

                flag += 2

                r = r + 2
                lines.insert(r+1, openmp_criti + '\n')

                flag += 1
                i += 1
            elif operater[i] == 2:
                lines.insert(row_for, openmp_set(N) + '\n')
                lines.insert(row_for + 1, openmp_dad + '\n')
                row_for += 2
                row_for_end += 2

                flag += 2

                r = r + 2
                lines.insert(r+1, openmp_ato + '\n')

                flag += 1
                i += 1
    lines.insert(0, head+'\n')
    lines.insert(0, clock +'\n')
    for line in lines:
        f_.write(line)
    f.close()
    f_.close()

    os.system(r"gcc -fopenmp bing.c -o bing.exe")
    # os.system("python runCFile.py")
    runCFile.function1(N)

WEN("chuanxing.c", [17], [0], 6)