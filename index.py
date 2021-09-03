first_list = [2, 3, 4, 5]

# simple loop
def simple_loop(list):
    for x in list:
        print(x)

# linear search
def linear_search(list):
    for x in list:
        if x == 2:
            print('list includes 2')

simple_loop(first_list)
linear_search(first_list)
