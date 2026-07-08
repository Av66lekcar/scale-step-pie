# -*- coding: utf-8 -*-

import bpy


from bpy.types import (
    Menu,
    Operator,
)


from . import utils






# =====================================================
# PIE MENU
# =====================================================


class VIEW3D_MT_scale_step_pie(Menu):


    bl_label = "Scale Step Pie"




    def draw(self, context):


        pie = self.layout.menu_pie()



        prefs = utils.get_preferences()



        slots = []

        if prefs:

            slots = list(
                prefs.slots
            )





        # 1 TOP
        if len(slots) > 0:

            op = pie.operator(
                "object.scale_step_v240",
                text=slots[0].label
            )

            op.value = slots[0].value
            op.mode = slots[0].mode





        # 2 TOP RIGHT
        if len(slots) > 1:

            op = pie.operator(
                "object.scale_step_v240",
                text=slots[1].label
            )

            op.value = slots[1].value
            op.mode = slots[1].mode





        # 3 RIGHT
        if len(slots) > 2:

            op = pie.operator(
                "object.scale_step_v240",
                text=slots[2].label
            )

            op.value = slots[2].value
            op.mode = slots[2].mode





        # 4 BOTTOM RIGHT
        if len(slots) > 3:

            op = pie.operator(
                "object.scale_step_v240",
                text=slots[3].label
            )

            op.value = slots[3].value
            op.mode = slots[3].mode





        # 5 BOTTOM
        op = pie.operator(
            "object.scale_reset_v240",
            text="Reset Scale"
        )





        # 6 BOTTOM LEFT
        if len(slots) > 4:

            op = pie.operator(
                "object.scale_step_v240",
                text=slots[4].label
            )

            op.value = slots[4].value
            op.mode = slots[4].mode





        # 7 LEFT
        if len(slots) > 5:

            op = pie.operator(
                "object.scale_step_v240",
                text=slots[5].label
            )

            op.value = slots[5].value
            op.mode = slots[5].mode





        # 8 TOP LEFT
        op = pie.operator(
            "object.apply_scale_v240",
            text="Apply Scale"
        )









# =====================================================
# OPEN PIE OPERATOR
# =====================================================


class VIEW3D_OT_scale_step_pie(Operator):


    bl_idname = "view3d.scale_step_pie"


    bl_label = "Scale Step Pie"


    bl_description = (
        "Open Scale Step Pie Menu"
    )


    bl_options = {
        "REGISTER"
    }





    def execute(
            self,
            context
    ):


        bpy.ops.wm.call_menu_pie(
            name="VIEW3D_MT_scale_step_pie"
        )


        return {
            "FINISHED"
        }









classes = (

    VIEW3D_MT_scale_step_pie,

    VIEW3D_OT_scale_step_pie,

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
