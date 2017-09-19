#1
with open("stat", 'r') as f:
    content = f.readlines()
print("Zadanie 1 wynik")
for line in content:
    print(line)

#2
# - user: normal processes executing in user mode
# - nice: niced processes executing in user mode
# - system: processes executing in kernel mode
# - idle: twiddling thumbs
# - iowait: In a word, iowait stands for waiting for I/O to complete. But there
#   are several problems:
#   1. Cpu will not wait for I/O to complete, iowait is the time that a task is
#      waiting for I/O to complete. When cpu goes into idle state for
#      outstanding task io, another task will be scheduled on this CPU.
#   2. In a multi-core CPU, the task waiting for I/O to complete is not running
#      on any CPU, so the iowait of each CPU is difficult to calculate.
#   3. The value of iowait field in /proc/stat will decrease in certain
#      conditions.
#   So, the iowait is not reliable by reading from /proc/stat.
# - irq: servicing interrupts
# - softirq: servicing softirqs
# - steal: involuntary wait
# - guest: running a normal guest
# - guest_nice: running a niced guest
with open("stat", 'r') as f:
    content = f.readlines()
print("Zadanie 2 wynik")
for line in content:
    if line.startswith("cpu"):
        values = line.split()
        print("user time spent for " + values[0] + ": " + values[1])

#3
#helper method
def percentage(idx, val):
    if len(val) < 11:
        return -1
    # ( idle * 100 ) / ( user + nice + system + idle + iowait + irq + softirq + steal + guest + guest_nice)
    return (int(val[idx]) * 100) / (int(val[1]) + int(val[2]) + int(val[3]) + int(val[4]) + int(val[5]) + int(val[6]) +
                                    int(val[7]) + int(val[8]) + int(val[9]) + int(val[10]))

with open("stat", 'r') as f:
    content = f.readlines()
print("Zadanie 3 wynik")
for line in content:
    if line.startswith("cpu"):
        values = line.split()
        print("idle percentage for " + values[0] + ": " + str(percentage(4, values)))
#4
with open("stat", 'r') as f:
    content = f.readlines()
count = 0
for line in content:
    if line.startswith("cpu"):
        count += 1
print("Zadanie 4 wynik")
print("total logical cores count = " + str(count - 1))

#5
with open("stat", 'r') as f:
    content = f.readlines()
print("Zadanie 5 wynik")
for line in content:
    if line.startswith("processes"):
        values = line.split()
        print("Processes count: " + values[1])

#6
with open("stat", 'r') as f:
    content = f.readlines()
print("Zadanie 6 wynik")
for line in content:
    if line.startswith("procs_running"):
        values = line.split()
        print("Processes running count: " + values[1])
