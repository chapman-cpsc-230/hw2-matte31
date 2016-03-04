k = 0.055

T_str = raw_input("What is the Temperature of the tea?: ")
T = float(T_str)

T_a_str = raw_input("What is the Temperature of the room?:")
T_a = float(T_a_str)

M_str = raw_input("How long has the Tea been out?:")
M = int(M_str)

minute = 0
t = T

print "Minute   Temperature"

while minute < M:
    t += -k*(T - T_a)
    print "%4.1g   %10.2f" %(minute,t)
    minute += 1
