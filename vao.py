from shader_program import ShaderProgram
from vbo import VBO


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos["cube"] = self.get_vao(program=self.program.programs["default"], vbo=self.vbo.vbos["cube"])

        # shadow cube vao
        self.vaos["shadow_cube"] = self.get_vao(program=self.program.programs["shadow_map"], vbo=self.vbo.vbos["cube"])

        # cat vao
        self.vaos["cat"] = self.get_vao(program=self.program.programs["default"], vbo=self.vbo.vbos["cat"])

        self.vaos["low_poly_tree_bark"] = self.get_vao(
            program=self.program.programs["default"], vbo=self.vbo.vbos["low_poly_tree_bark"]
        )
        self.vaos["shadow_low_poly_tree_bark"] = self.get_vao(
            program=self.program.programs["shadow_map"], vbo=self.vbo.vbos["low_poly_tree_bark"]
        )
        self.vaos["low_poly_tree_tree"] = self.get_vao(
            program=self.program.programs["default"], vbo=self.vbo.vbos["low_poly_tree_tree"]
        )
        self.vaos["shadow_low_poly_tree_tree"] = self.get_vao(
            program=self.program.programs["shadow_map"], vbo=self.vbo.vbos["low_poly_tree_tree"]
        )
        self.vaos["wolf_body"] = self.get_vao(program=self.program.programs["default"], vbo=self.vbo.vbos["wolf_body"])
        self.vaos["shadow_wolf_body"] = self.get_vao(
            program=self.program.programs["shadow_map"], vbo=self.vbo.vbos["wolf_body"]
        )
        self.vaos["wolf_claws"] = self.get_vao(
            program=self.program.programs["default"], vbo=self.vbo.vbos["wolf_claws"]
        )
        self.vaos["shadow_wolf_claws"] = self.get_vao(
            program=self.program.programs["shadow_map"], vbo=self.vbo.vbos["wolf_claws"]
        )
        self.vaos["wolf_eyes"] = self.get_vao(program=self.program.programs["default"], vbo=self.vbo.vbos["wolf_eyes"])
        self.vaos["shadow_wolf_eyes"] = self.get_vao(
            program=self.program.programs["shadow_map"], vbo=self.vbo.vbos["wolf_eyes"]
        )
        self.vaos["wolf_fur"] = self.get_vao(program=self.program.programs["default"], vbo=self.vbo.vbos["wolf_fur"])
        self.vaos["shadow_wolf_fur"] = self.get_vao(
            program=self.program.programs["shadow_map"], vbo=self.vbo.vbos["wolf_fur"]
        )
        self.vaos["wolf_teeth"] = self.get_vao(
            program=self.program.programs["default"], vbo=self.vbo.vbos["wolf_teeth"]
        )
        self.vaos["shadow_wolf_teeth"] = self.get_vao(
            program=self.program.programs["shadow_map"], vbo=self.vbo.vbos["wolf_teeth"]
        )

        # shadow cat vao
        self.vaos["shadow_cat"] = self.get_vao(program=self.program.programs["shadow_map"], vbo=self.vbo.vbos["cat"])

        # skybox vao
        self.vaos["skybox"] = self.get_vao(program=self.program.programs["skybox"], vbo=self.vbo.vbos["skybox"])

        # advanced_skybox vao
        self.vaos["advanced_skybox"] = self.get_vao(
            program=self.program.programs["advanced_skybox"], vbo=self.vbo.vbos["advanced_skybox"]
        )

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
