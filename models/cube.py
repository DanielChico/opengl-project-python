from models.base_model import ExtendedBaseModel


class Cube(ExtendedBaseModel):
    def __init__(self, app, vao_name="cube", tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
