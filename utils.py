# -*- coding: utf-8 -*-

import bpy





# =====================================================
# GET ADDON PREFERENCES
# =====================================================


def get_preferences():


    addon = bpy.context.preferences.addons.get(

        __package__

    )


    if addon:

        return addon.preferences



    return None







# =====================================================
# SCALE CALCULATION
# =====================================================


def calculate_scale(

        current,

        value,

        mode

):


    if mode == "ADD":


        return current + value




    elif mode == "MULTIPLY":


        return current * value




    elif mode == "DIVIDE":


        if value != 0:

            return current / value



    return current







# =====================================================
# PROTECT SCALE
# =====================================================


def clamp_scale(

        value,

        protect=True

):


    if protect:


        return max(

            value,

            0.0

        )



    return value







# =====================================================
# APPLY SCALE
# =====================================================


def apply_scale(

        obj,

        value,

        mode="ADD",

        axis="XYZ",

        protect=True

):


    scale = list(

        obj.scale

    )



    if axis in {"XYZ", "X"}:


        scale[0] = clamp_scale(

            calculate_scale(

                scale[0],

                value,

                mode

            ),

            protect

        )




    if axis in {"XYZ", "Y"}:


        scale[1] = clamp_scale(

            calculate_scale(

                scale[1],

                value,

                mode

            ),

            protect

        )




    if axis in {"XYZ", "Z"}:


        scale[2] = clamp_scale(

            calculate_scale(

                scale[2],

                value,

                mode

            ),

            protect

        )




    obj.scale = scale







# =====================================================
# FORMAT VALUES FOR UI
# =====================================================


def format_step(

        value

):


    if value > 0:

        return f"+{value:.3f}"



    return f"{value:.3f}"
# =====================================================
# REGISTER
# =====================================================

def register():
    pass


def unregister():
    pass
