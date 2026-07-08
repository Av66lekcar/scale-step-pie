# -*- coding: utf-8 -*-

import bpy


addon_keymaps = []





def register():


    wm = bpy.context.window_manager


    if wm is None:

        return



    kc = wm.keyconfigs.addon


    if kc is None:

        return





    km = kc.keymaps.new(

        name="3D View",

        space_type="VIEW_3D"

    )





    kmi = km.keymap_items.new(

        "view3d.scale_step_pie",

        type="S",

        value="PRESS",

        ctrl=True,

        shift=True

    )





    addon_keymaps.append(

        (

            km,

            kmi

        )

    )









def unregister():


    for km, kmi in addon_keymaps:


        try:

            km.keymap_items.remove(kmi)


        except:

            pass



    addon_keymaps.clear()
