__author__ = 'alpha'

def solve_list(lst):
    if len(lst) <= 3:
        to_be_appended = 0
        for values in range((len(lst))):
            to_be_appended += lst[values]
        print(to_be_appended)
        lst.append(to_be_appended)
    else:
        to_be_appended = 0
        index = 1
        while index <= 3:
            to_be_appended += lst[-index]
            index += 1
        print(to_be_appended)
        lst.append(to_be_appended)



lst = [0,1,2]
for i in range(25):
    solve_list(lst)
print(lst[20])