from models.base_model import ExtendedBaseModel


class Cat(ExtendedBaseModel):
    def __init__(self, app, vao_name="cat", tex_id="cat", pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
