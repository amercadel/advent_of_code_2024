import sys
import re

def find_multiplications(input_str):
    regex_pattern = r"mul\(\d+,\d+\)"
    mults = re.findall(regex_pattern, input_str)
    return mults

def parse_multiplication(multiplication: str):
    multiplication = multiplication.replace("mul(", "").replace(")", "").split(",")
    multiplication = list(map(int, multiplication))
    return multiplication[0] * multiplication[1]

def parse_multiplications(multiplications: list[str]):
    s = 0
    for mult in multiplications:
        s += parse_multiplication(mult)
    return s


def find_dos(input_str):
    dos = input_str.split("do()")
    s = 0
    for i in dos:
        p = i.split("don't()")[0]
        mults = find_multiplications(p)
        val = parse_multiplications(mults)
        s += val
    return s

        


    



def main():
    input_file = sys.argv[1]
    f = open(input_file)
    data = f.read()
    f.close()
    data = data.strip()
    mults = find_multiplications(data)
    val = parse_multiplications(mults)
    print(val)
    dos = find_dos(data)
    print(dos)
    
        



if __name__ == "__main__":
    main()