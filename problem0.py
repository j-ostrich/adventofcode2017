    class Grid(object):
        def __init__(self, input_):
            self.markers = {"A": set(), "B": set()}
            split_input = input_.strip().split(", ")
            cur_pos = [0, 0]
            for direction in split_input:
                op = self.handle_direction(direction)
                if op:
                    cur_pos = [cur_pos[0] + op[0], cur_pos[1] + op[1]]
                else:
                    if direction == "Start":
                        break
                    else:
                        self.markers[direction].add(tuple(cur_pos))

        @staticmethod
        def handle_direction(direction):
            if direction == "Left":
                return (-1, 0)
            elif direction == "Right":
                return (1, 0)
            elif direction == "Up":
                return (0, 1)
            elif direction == "Down":
                return (0, -1)
            return None

        def max_distance_from_origin(self):
            return max(abs(m[0]) + abs(m[1]) for m in self.markers["A"] & self.markers["B"])

        def max_distance_in_pair(self):
            return max(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a in self.markers["A"] for b in self.markers["B"])


    if __name__ == '__main__':
        with open("problem0_input.txt") as f:
            grid = Grid(f.readline())
        print("Part 1: %s" % grid.max_distance_from_origin())
        print("Part 2: %s" % grid.max_distance_in_pair())
