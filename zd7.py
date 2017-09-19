def percentage(idx, val):
    if len(val) < 11:
        return -1
    # ( idle * 100 ) / ( user + nice + system + idle + iowait + irq + softirq + steal + guest + guest_nice)
    return (int(val[idx]) * 100) / (int(val[1]) + int(val[2]) + int(val[3]) + int(val[4]) + int(val[5]) + int(val[6]) +
                                    int(val[7]) + int(val[8]) + int(val[9]) + int(val[10]))

def parse_content(cntnt):
    cont = {}
    for line in cntnt:
        values = line.split()
        if "cpu" in values[0]:
            cont[values[0]] = {
                "user": percentage(1, values),
                "nice": percentage(2, values),
                "system": percentage(3, values),
                "idle": percentage(4, values),
                "iowait": percentage(5, values),
                "irq": percentage(6, values),
                "softirq": percentage(7, values),
                "steal": percentage(8, values),
                "guest": percentage(9, values),
                "guest_nice": percentage(10, values)
            }
        else:
            cont[values[0]] = values[1]
    return cont

with open("stat", 'r') as f:
    content = f.readlines()
cn = parse_content(content)
inpt = ""
while inpt != 'q':
    inpt = input("What do you want to know? Press h for help, q for quit\n")
    if inpt == 'q':
        print("exiting")
        continue
    if inpt == "h":
        print("possible commands")
        for key in cn:
            if "cpu" in key:
                for k in cn[key]:
                    print(key, k)
            else:
                print(key)
        continue
    inp_cnt = inpt.split()
    if len(inp_cnt) == 2:
        if inp_cnt[0] not in cn or inp_cnt[1] not in cn[inp_cnt[0]]:
            print("invalid command")
            continue
        print(inpt + " = " + str(cn[inp_cnt[0]][inp_cnt[1]]))
    else:
        if inpt not in cn:
            print("invalid command")
            continue
        print(inpt + " = " + str(cn[inpt]))
