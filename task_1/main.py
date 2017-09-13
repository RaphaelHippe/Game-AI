def successors(X, Y):
    def sc(state):
        x, y = state
        assert x <= X and y <= Y
        return {(X, y): 'fill x',
                (x, Y): 'fill y',
                (0, y): 'empty x',
                (x, 0): 'empty y',
                (fillXToY(X, x, Y, y)): 'fill X to Y',
                (fillYToX(X, x, Y, y)): 'fill Y to X',

        }
    return sc

def fillXToY(X, x, Y, y):
    return fill(X, x, Y, y)

def fillYToX(X, x, Y, y):
    # y, x = fill(Y, y, X, x)
    return tuple(reversed(fill(Y, y, X, x)))

def fill(origin_max, origin_current, destination_max, destination_current):
    dest_space_left = destination_max - destination_current
    if (dest_space_left <= 0) or (origin_current == 0):
        return (origin_current, destination_current)

    if origin_current - dest_space_left >= 0:
        # origin glas wird nicht leer
        origin_current -= dest_space_left
        destination_current = destination_max
        return (origin_current, destination_current)

    if origin_current - dest_space_left < 0:
        destination_current += origin_current
        origin_current = 0
        return (origin_current, destination_current)


'''
Created on Sep 15, 2013

@author: pglauner
'''
def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []

if __name__ == '__main__':
    res = shortest_path_search((0, 0), successors(418, 986), lambda state: state == (6, 0))
    print res
    print '%s transitions' % (len(res) / 2)
