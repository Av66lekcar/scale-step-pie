# -*- coding: utf-8 -*-

import bpy


from bpy.types import (
    AddonPreferences,
    PropertyGroup,
)


from bpy.props import (
    FloatProperty,
    EnumProperty,
    BoolProperty,
    StringProperty,
    CollectionProperty,
)





MODE_ITEMS = (
    ("ADD", "Add", "Add value"),
    ("MULTIPLY", "Multiply", "Multiply scale"),
    ("DIVIDE", "Divide", "Divide scale"),
)



AXIS_ITEMS = (
    ("XYZ", "XYZ", "All axes"),
    ("X", "X", "X axis"),
    ("Y", "Y", "Y axis"),
    ("Z", "Z", "Z axis"),
)







class SCALESTEPPIE_Slot(PropertyGroup):


    label: StringProperty(
        name="Label",
        default="STEP"
    )


    value: FloatProperty(
        name="Value",
        default=0.1,
        precision=4
    )


    mode: EnumProperty(
        name="Mode",
        items=MODE_ITEMS,
        default="ADD"
    )







def ensure_slots(prefs):


    if len(prefs.slots) >= 8:

        return



    defaults = (

        ("BIG +", 0.5),
        ("MEDIUM +", 0.1),
        ("SMALL +", 0.05),
        ("FINE +", 0.01),
        ("FINE -", -0.01),
        ("SMALL -", -0.05),
        ("MEDIUM -", -0.1),
        ("BIG -", -0.5),

    )



    while len(prefs.slots) < 8:


        index = len(prefs.slots)


        slot = prefs.slots.add()


        slot.label = defaults[index][0]

        slot.value = defaults[index][1]

        slot.mode = "ADD"









class SCALESTEPPIE_Preferences(
        AddonPreferences
):


    bl_idname = __package__





    axis: EnumProperty(
        name="Axis",
        items=AXIS_ITEMS,
        default="XYZ"
    )



    protect_negative: BoolProperty(
        name="Protect Negative",
        default=True
    )



    step_large: FloatProperty(
        name="Large",
        default=0.5
    )


    step_medium: FloatProperty(
        name="Medium",
        default=0.1
    )


    step_small: FloatProperty(
        name="Small",
        default=0.05
    )





    slots: CollectionProperty(
        type=SCALESTEPPIE_Slot
    )







    def draw(self, context):


        ensure_slots(self)



        layout = self.layout



        box = layout.box()

        box.label(
            text="Scale Step Pie v2.4.0 beta1"
        )





        box = layout.box()

        box.label(
            text="General"
        )


        box.prop(
            self,
            "axis",
            expand=True
        )


        box.prop(
            self,
            "protect_negative"
        )







        box = layout.box()

        box.label(
            text="Default Scale Steps"
        )


        row = box.row(
            align=True
        )


        row.prop(
            self,
            "step_large"
        )


        row.prop(
            self,
            "step_medium"
        )


        row.prop(
            self,
            "step_small"
        )







        box = layout.box()

        box.label(
            text="Pie Slots"
        )



        for index, slot in enumerate(self.slots):


            row = box.row(
                align=True
            )


            row.label(
                text=str(index + 1)
            )


            row.prop(
                slot,
                "label",
                text=""
            )


            row.prop(
                slot,
                "value",
                text=""
            )


            row.prop(
                slot,
                "mode",
                text=""
            )







classes = (

    SCALESTEPPIE_Slot,

    SCALESTEPPIE_Preferences,

)







def register():


    for cls in classes:

        bpy.utils.register_class(
            cls
        )







def unregister():


    for cls in reversed(classes):

        bpy.utils.unregister_class(
            cls
        )
