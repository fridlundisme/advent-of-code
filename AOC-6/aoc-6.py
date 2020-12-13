import re

if __name__ == "__main__":
    with open("input.in") as input_file:
        global_count = 0
        
        groupQ = set()
        group_members = 0
        for line in input_file:
            if line == '\n':
                global_count = global_count + len(groupQ)
                groupQ.clear()
                group_members = 0
                continue
            if(group_members) == 0:
                groupQ.update(line.rstrip())
                group_members = group_members +1
            else:
                intersect = groupQ.intersection(line.rstrip())
                groupQ = intersect
                group_members = group_members +1
        # + len(groupQ) is to add the last group count
        print("# Questions: ",global_count + len(groupQ))