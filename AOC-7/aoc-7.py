import re

def get_bags(line):
    can_hold_shinygold = 0
    number_regex = re.compile('[0-9]')
    test_regex = re.search(number_regex,line)
    split_line = line.split()
    bags_split = line.split('bag')
    main_bag = f'{split_line[0]}{split_line[1]}'
    main_bag_dict = dict
    bag_list = []
    for i,s in enumerate(split_line):
        if re.search(number_regex,s):
            bag_list.append(split_line[i+1] + split_line[i+2])
    main_bag_dict = {main_bag:bag_list}

    can_hold_shinygold = 1 if bag_list.count('shinygold') else 0
    return main_bag_dict,can_hold_shinygold

def add_bag():
    pass

def main():
    with open("test.in") as input_file:
        color_dict = {}
        binary_dict = {}
        for line in input_file:
            bag_dict, shinygold = get_bags(line)
            primary = list(bag_dict)[0]
            color_dict.update(bag_dict)
            binary_dict[primary] = shinygold
            print()


if __name__ == "__main__":
    main()