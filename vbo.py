import numpy as np
import pywavefront


class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos["cube"] = CubeVBO(ctx)
        self.vbos["cat"] = CatVBO(ctx)
        self.vbos["low_poly_tree_bark"] = LowPolyTreeBarkVBO(ctx)
        self.vbos["low_poly_tree_tree"] = LowPolyTreeTreeVBO(ctx)
        self.vbos["wolf_body"] = WolfBodyVBO(ctx)
        self.vbos["wolf_claws"] = WolfClawsVBO(ctx)
        self.vbos["wolf_eyes"] = WolfEyesVBO(ctx)
        self.vbos["wolf_fur"] = WolfFurVBO(ctx)
        self.vbos["wolf_teeth"] = WolfTeethVBO(ctx)
        self.vbos["skybox"] = SkyBoxVBO(ctx)
        self.vbos["advanced_skybox"] = AdvancedSkyBoxVBO(ctx)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]


class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attribs: list = None

    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()


class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = "2f 3f 3f"
        self.attribs = ["in_texcoord_0", "in_normal", "in_position"]

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype="f4")

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

        indices = [
            (0, 2, 3),
            (0, 1, 2),
            (1, 7, 2),
            (1, 6, 7),
            (6, 5, 4),
            (4, 7, 6),
            (3, 4, 5),
            (3, 5, 0),
            (3, 7, 4),
            (3, 2, 7),
            (0, 6, 1),
            (0, 5, 6),
        ]
        vertex_data = self.get_data(vertices, indices)

        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [
            (0, 2, 3),
            (0, 1, 2),
            (0, 2, 3),
            (0, 1, 2),
            (0, 1, 2),
            (2, 3, 0),
            (2, 3, 0),
            (2, 0, 1),
            (0, 2, 3),
            (0, 1, 2),
            (3, 1, 2),
            (3, 0, 1),
        ]
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        normals = [
            (0, 0, 1) * 6,
            (1, 0, 0) * 6,
            (0, 0, -1) * 6,
            (-1, 0, 0) * 6,
            (0, 1, 0) * 6,
            (0, -1, 0) * 6,
        ]
        normals = np.array(normals, dtype="f4").reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data


class CatVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = "2f 3f 3f"
        self.attribs = ["in_texcoord_0", "in_normal", "in_position"]

    def get_vertex_data(self):
        objs = pywavefront.Wavefront("objects/cat/20430_Cat_v1_NEW.obj", cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype="f4")
        return vertex_data


class LowPolyTreeBarkVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = "2f 3f 3f"
        self.attribs = ["in_texcoord_0", "in_normal", "in_position"]

    def get_vertex_data(self):
        objs = pywavefront.Wavefront("objects/low_poly_tree/Lowpoly_tree_sample.obj", cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype="f4")
        return vertex_data


class LowPolyTreeTreeVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = "2f 3f 3f"
        self.attribs = ["in_texcoord_0", "in_normal", "in_position"]

    def get_vertex_data(self):
        objs = pywavefront.Wavefront("objects/low_poly_tree/Lowpoly_tree_sample.obj", cache=True, parse=True)
        objs.materials.popitem()
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype="f4")
        return vertex_data


class WolfBodyVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = "2f 3f 3f"
        self.attribs = ["in_texcoord_0", "in_normal", "in_position"]

    def get_vertex_data(self):
        objs = pywavefront.Wavefront("objects/wolf/Wolf_One_obj.obj", cache=True, parse=True)
        for name, material in objs.materials.items():
            if name == "Wolf_Body":
                vertex_data = material.vertices
                vertex_data = np.array(vertex_data, dtype="f4")
                return vertex_data


class WolfClawsVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = "2f 3f 3f"
        self.attribs = ["in_texcoord_0", "in_normal", "in_position"]

    def get_vertex_data(self):
        objs = pywavefront.Wavefront("objects/wolf/Wolf_One_obj.obj", cache=True, parse=True)
        for name, material in objs.materials.items():
            if name == "Wolf_Claws":
                vertex_data = material.vertices
                vertex_data = np.array(vertex_data, dtype="f4")
                return vertex_data


class WolfEyesVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = "2f 3f 3f"
        self.attribs = ["in_texcoord_0", "in_normal", "in_position"]

    def get_vertex_data(self):
        objs = pywavefront.Wavefront("objects/wolf/Wolf_One_obj.obj", cache=True, parse=True)
        for name, material in objs.materials.items():
            if name == "Wolf_Eyes":
                vertex_data = material.vertices
                vertex_data = np.array(vertex_data, dtype="f4")
                return vertex_data


class WolfFurVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = "2f 3f 3f"
        self.attribs = ["in_texcoord_0", "in_normal", "in_position"]

    def get_vertex_data(self):
        objs = pywavefront.Wavefront("objects/wolf/Wolf_One_obj.obj", cache=True, parse=True)
        for name, material in objs.materials.items():
            if name == "Wolf_Fur":
                vertex_data = material.vertices
                vertex_data = np.array(vertex_data, dtype="f4")
                return vertex_data


class WolfTeethVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = "2f 3f 3f"
        self.attribs = ["in_texcoord_0", "in_normal", "in_position"]

    def get_vertex_data(self):
        objs = pywavefront.Wavefront("objects/wolf/Wolf_One_obj.obj", cache=True, parse=True)
        for name, material in objs.materials.items():
            if name == "Wolf_Teeth":
                vertex_data = material.vertices
                vertex_data = np.array(vertex_data, dtype="f4")
                return vertex_data


class SkyBoxVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = "3f"
        self.attribs = ["in_position"]

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype="f4")

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

        indices = [
            (0, 2, 3),
            (0, 1, 2),
            (1, 7, 2),
            (1, 6, 7),
            (6, 5, 4),
            (4, 7, 6),
            (3, 4, 5),
            (3, 5, 0),
            (3, 7, 4),
            (3, 2, 7),
            (0, 6, 1),
            (0, 5, 6),
        ]
        vertex_data = self.get_data(vertices, indices)
        vertex_data = np.flip(vertex_data, 1).copy(order="C")
        return vertex_data


class AdvancedSkyBoxVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = "3f"
        self.attribs = ["in_position"]

    def get_vertex_data(self):
        # in clip space
        z = 0.9999
        vertices = [(-1, -1, z), (3, -1, z), (-1, 3, z)]
        vertex_data = np.array(vertices, dtype="f4")
        return vertex_data
