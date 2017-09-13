import sys

def tree(visible, distance, armed, flank):
    if visible:
        if distance < 10:
            return "attack!"
        else:
            if flank:
                return "move!"
            else:
                return "attack!!"
    else:
        if armed:
            return "attack!"
        else:
            return "creep!"


if len(sys.argv) == 5:
    print bool(sys.argv[1]) is bool, sys.argv[2], sys.argv[3], sys.argv[4]
    print tree(bool(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4])
else:
    print "YOU FAILED!"

# best script ever :D
