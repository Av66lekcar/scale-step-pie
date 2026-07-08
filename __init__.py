# -*- coding: utf-8 -*-

bl_info = {
    "name": "Scale Step Pie v2.4.0 alpha2",
    "author": "OpenAI",
    "version": (2, 4, 0),
    "blender": (5, 0, 0),
    "location": "3D View > Pie Menu",
    "description": "Customizable Scale Step Pie Menu",
    "category": "Object",
}


import bpy


from . import preferences
from . import operators
from . import pie_menu
from . import keymap
from . import utils





modules = (

    preferences,
    operators,
    pie_menu,
    keymap,
    utils,

)





def initialize_slots():


    addon = bpy.context.preferences.addons.get(
        __package__
    )


    if addon is None:

        return



    prefs = addon.preferences



    if len(prefs.slots) > 0:

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





    for label, value in defaults:


        slot = prefs.slots.add()


        slot.label = label

        slot.value = value

        slot.mode = "ADD"







def register():


    for module in modules:

        module.register()



    bpy.app.timers.register(
        initialize_slots,
        first_interval=0.1
    )



    print(
        "Scale Step Pie v2.4.0 alpha2 fix3 loaded"
    )







def unregister():


    for module in reversed(modules):

        module.unregister()





if __name__ == "__main__":

    register()
