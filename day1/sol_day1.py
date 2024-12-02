import sys

def parse_input(input_file: str) -> tuple[list]:
    f = open(input_file)
    data = f.readlines()
    f.close()
    data = [i.strip().split() for i in data]
    lst1 = [int(i[0]) for i in data]
    lst2 = [int(i[1]) for i in data]
    return lst1, lst2

def distance(lst1, lst2):
    lst1.sort()
    lst2.sort()
    running_sum = 0
    for i in range(len(lst1)):
        val = abs(lst1[i] - lst2[i])
        running_sum += val
    return running_sum


def similarity(lst1, lst2):
    # we want to find out how many times each element in lst1 appears in l2
    counter = {}
    for i in lst2:
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 1
    similarity = 0
    for val in lst1:
        if val not in counter.keys():
            continue
        else:
            similarity += (val * counter[val])
    return similarity

    






def main():
    input_file = sys.argv[1]
    l1, l2 = parse_input(input_file)
    print(distance(l1, l2))
    print(similarity(l1, l2))
    


if __name__ == "__main__":
    main()