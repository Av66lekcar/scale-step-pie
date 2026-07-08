# -*- coding: utf-8 -*-

import bpy


from bpy.types import Operator


from bpy.props import (
    FloatProperty,
    EnumProperty,
)





from . import utils







# =====================================================
# SCALE STEP
# =====================================================


class OBJECT_OT_scale_step_v240(
        Operator
):


    bl_idname = "object.scale_step_v240"


    bl_label = "Scale Step"


    bl_description = (
        "Apply scale step"
    )


    bl_options = {
        "REGISTER",
        "UNDO"
    }





    value: FloatProperty(
        name="Value",
        default=0.1
    )



    mode: EnumProperty(
        name="Mode",
        items=(
            ("ADD", "Add", ""),
            ("MULTIPLY", "Multiply", ""),
            ("DIVIDE", "Divide", ""),
        ),
        default="ADD"
    )







    def execute(self, context):


        prefs = utils.get_preferences()



        if prefs is None:

            return {
                'CANCELLED'
            }





        for obj in context.selected_objects:


            utils.apply_scale(

                obj,

                self.value,

                self.mode,

                prefs.axis,

                prefs.protect_negative

            )



        return {
            'FINISHED'
        }









# =====================================================
# RESET SCALE
# =====================================================


class OBJECT_OT_scale_reset_v240(
        Operator
):


    bl_idname = "object.scale_reset_v240"


    bl_label = "Reset Scale"


    bl_description = (
        "Reset object scale to 1"
    )


    bl_options = {
        "REGISTER",
        "UNDO"
    }





    def execute(self, context):


        for obj in context.selected_objects:


            obj.scale = (
                1.0,
                1.0,
                1.0
            )



        return {
            'FINISHED'
        }









# =====================================================
# APPLY SCALE
# =====================================================


class OBJECT_OT_apply_scale_v240(
        Operator
):


    bl_idname = "object.apply_scale_v240"


    bl_label = "Apply Scale"


    bl_description = (
        "Apply object scale"
    )


    bl_options = {
        "REGISTER",
        "UNDO"
    }





    def execute(self, context):


        bpy.ops.object.transform_apply(
            location=False,
            rotation=False,
            scale=True
        )



        return {
            'FINISHED'
        }









classes = (

    OBJECT_OT_scale_step_v240,

    OBJECT_OT_scale_reset_v240,

    OBJECT_OT_apply_scale_v240,

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
