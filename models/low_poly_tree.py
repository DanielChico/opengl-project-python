from models.base_model import ExtendedBaseModel, MultiModel


class LowPolyTreeBark(ExtendedBaseModel):
    def __init__(
        self,
        app,
        vao_name="low_poly_tree_bark",
        tex_id="low_poly_tree_bark",
        pos=(0, 0, 0),
        rot=(0, 0, 0),
        scale=(1, 1, 1),
    ):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class LowPolyTreeTree(ExtendedBaseModel):
    def __init__(
        self,
        app,
        vao_name="low_poly_tree_tree",
        tex_id="low_poly_tree_tree",
        pos=(0, 0, 0),
        rot=(0, 0, 0),
        scale=(1, 1, 1),
    ):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class LowPolyTree(MultiModel):
    def __init__(self, app, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)) -> None:
        models = [
            LowPolyTreeBark(app, pos=pos, rot=rot, scale=scale),
            LowPolyTreeTree(app, pos=pos, rot=rot, scale=scale),
        ]
        super().__init__(models)
