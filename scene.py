import random

from model import Cat, Cube, LowPolyTreeBark, LowPolyTreeTree


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        # self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # floor
        n, s = 80, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))
        #
        x, y = 0, 0
        num_of_cubes = 10
        center = (num_of_cubes * 2) / 2
        for i in range(num_of_cubes):
            x2 = x + num_of_cubes * 2 - i * 2
            for z in range(1, 20, 2):
                add(Cube(app, pos=(x, y, z)))
                add(Cube(app, pos=(x2 + 20, y, z)))
                add(Cube(app, pos=(center + z, y, x - num_of_cubes)))
                add(Cube(app, pos=(center + z, y, x2 - num_of_cubes + 20)))
            x += 1
            y += 2
        for w in range(num_of_cubes * 2, num_of_cubes * 2 + 20, 2):
            for v in range(num_of_cubes * -1, num_of_cubes * -1 * 2 - 20, 2):
                add(Cube(app, pos=(w, y, v)))

        # # columns
        # for i in range(9):
        #     add(Cube(app, pos=(15, i * s, -9 + i), tex_id=2))
        #     add(Cube(app, pos=(15, i * s, 5 - i), tex_id=2))

        # cat
        add(Cat(app, pos=(0, -1, -10)))
        # add(Cottage(app, pos=(0, -1, -10)))
        for _ in range(20):
            x = random.randint(-50, 50)
            z = random.randint(-50, 50)
            add(LowPolyTreeBark(app, pos=(x, -1, z)))
            add(LowPolyTreeTree(app, pos=(x, -1, z)))

        # moving cube
        # self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        # add(self.moving_cube)

    def update(self):
        pass
        # self.moving_cube.rot.xyz = self.app.time
