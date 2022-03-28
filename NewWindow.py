import bpy

# Modify render settings
render = bpy.context.scene.render
render.resolution_x = 640
render.resolution_y = 480
render.resolution_percentage = 100

# Modify preferences (to guaranty new window)
prefs = bpy.context.preferences
prefs.view.render_display_type = "WINDOW"

# Call image editor window
bpy.ops.render.view_show("INVOKE_DEFAULT")

# Change area type
area = bpy.context.window_manager.windows[-1].screen.areas[0]
area.type = "TEXT_EDITOR"

# Restore render settings and preferences
# render.resolution_x = original_value
# ...

# I also restore is_dirty tag which affects preferences autosave feature
# prefs.is_dirty = original_value

#Fontes:
#https://blender-stackexchange-com.translate.goog/questions/81974/new-window-with-python-api?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc
#https://docs.blender.org/api/current/bpy.types.Window.html