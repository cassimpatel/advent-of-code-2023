from z3 import Int, Solver
import z3

def day24_part1(input, min, max):
    points = [[int(y) for y in x.split(', ')] for x in input.replace(' @', ',').split('\n')]
    n = len(points)

    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            # fetch points, ignore z
            [x1, y1, _, dx1, dy1, _] = points[i]
            [x2, y2, _, dx2, dy2, _] = points[j]

            # calculate gradients and intercepts
            m1 = dy1 / dx1
            m2 = dy2 / dx2
            b1 = -m1 * x1 + y1
            b2 = -m2 * x2 + y2

            # ignore parallel lines
            if m1 == m2: continue

            # calculate intersection
            x_int = (b2 - b1)/(m1 - m2)
            y_int = m1 * x_int + b1

            # ignore if intercept not in bounds
            if not min <= x_int <= max: continue
            if not min <= y_int <= max: continue

            # calculate time of intercept, ignore if in past
            t1 = (x_int - x1) / dx1
            t2 = (x_int - x2) / dx2
            if t1 < 0 or t2 < 0: continue
            res += 1

    return res

def day24_part2(input):
    # only take first three points, that's all we need
    points = [[int(y) for y in x.split(', ')] for x in input.replace(' @', ',').split('\n')]
    points = points[:3]

    # set our unknowns: starting position, and velocities
    x, y, z, dx, dy, dz = Int('x'), Int('y'), Int('z'), Int('dx'), Int('dy'), Int('dz')
    s = Solver()

    for i in range(3):
        [xi, yi, zi, dxi, dyi, dzi] = points[i]
        # additional unknown for when this hailstone collides with the magic stone
        t = Int(f't_{i}')

        # add constraint so the collision is in the future
        s.add(t >= 0)

        # constraint so after t nanoseconds, the magic stone and the hail stone are in the same point (for x, y, and z)
        s.add(x + dx * t == xi + dxi * t)
        s.add(y + dy * t == yi + dyi * t)
        s.add(z + dz * t == zi + dzi * t)

    assert s.check() == z3.sat
    model = s.model()
    return model.eval(x + y + z)

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day24_part1(example_input, 7, 27) == 2
    print(day24_part1(test_input, 200000000000000, 400000000000000))

    assert day24_part2(example_input) == 47
    print(day24_part2(test_input))