import sys

def parse_reports(input_file: str):
    f = open(input_file)
    data = f.readlines()
    f.close()
    data = [i.strip().split(" ") for i in data]
    data = [list(map(int, x)) for x in data]
    return data

def check_safety(report: list[int]) -> bool:
    # first pass to check for increasing/decreasing
    inc = False
    dec = False
    idx = 0
    while ((inc != True) or (dec != True)) and (idx < len(report) - 1):
        curr = report[idx]
        next_ = report[idx + 1]
        if curr < next_:
            dec = True
        elif curr > next_:
            inc = True
        else:
            return False
        idx += 1
    if inc and dec:
        return False

    # second pass to check difference
    for i in range(len(report) - 1):
        curr = report[i]
        next_ = report[i + 1]
        diff = abs(curr - next_)
        if diff == 0 or diff > 3:
            return False
    return True


def check_safety_with_tolerance(report: list[int]) -> bool:
    for i in range(len(report)): # not ideal to loop through every possibility, but early return is helpful
        tmp = [report[j] for j in range(len(report)) if j != i]
        if check_safety(tmp):
            return True
    return False
    


        




def main():
    input_file = sys.argv[1]
    reports = parse_reports(input_file)
    safe_count = 0
    for i in reports:
        safe_count += int(check_safety_with_tolerance(i))
    print(safe_count)
    # print(check_safety([1, 3, 2, 4, 5]))
    


if __name__ == "__main__":
    main()
