from models.base_model import ExtendedBaseModel, MultiModel


class WolfBody(ExtendedBaseModel):
    def __init__(self, app, vao_name="wolf_body", tex_id="wolf_body", pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class WolfClaws(ExtendedBaseModel):
    def __init__(self, app, vao_name="wolf_claws", tex_id=1, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class WolfEyes(ExtendedBaseModel):
    def __init__(self, app, vao_name="wolf_eyes", tex_id="wolf_eyes", pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class WolfFur(ExtendedBaseModel):
    def __init__(self, app, vao_name="wolf_fur", tex_id="wolf_fur", pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class WolfTeeth(ExtendedBaseModel):
    def __init__(self, app, vao_name="wolf_teeth", tex_id=1, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)


class Wolf(MultiModel):
    def __init__(self, app, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)) -> None:
        models = [
            WolfBody(app, pos=pos, rot=rot, scale=scale),
            WolfClaws(app, pos=pos, rot=rot, scale=scale),
            WolfEyes(app, pos=pos, rot=rot, scale=scale),
            WolfFur(app, pos=pos, rot=rot, scale=scale),
            WolfTeeth(app, pos=pos, rot=rot, scale=scale),
        ]
        super().__init__(models)
