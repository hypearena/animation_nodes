import bpy
from .. preferences import getDeveloperSettings

class DeveloperPanel(bpy.types.Panel):
    bl_idname = "an_developer_panel"
    bl_label = "Developer"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "TOOLS"
    bl_category = "Animation Nodes"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        try: return context.space_data.node_tree.bl_idname == "an_AnimationNodeTree"
        except: return False

    def draw(self, context):
        layout = self.layout
        tree = context.space_data.node_tree

        col = layout.column()
        col.label("Execution Code:")

        developer = getDeveloperSettings()
        col.prop(developer, "monitoredExecution")

        row = col.row(align = True)
        row.operator("an.print_current_execution_code", text = "Print", icon = "CONSOLE")
        row.operator("an.write_current_execution_code", text = "Write", icon = "TEXT")

        layout.separator()

        profiling = developer.profiling

        col = layout.column()
        col.prop(profiling, "function", text = "Function")
        col.prop(profiling, "sort", text = "Sort Mode")
        col.prop(profiling, "output", text = "Output")

        subcol = col.column()
        subcol.scale_y = 1.3
        props = subcol.operator("an.profile", text = "Profile", icon = "PREVIEW_RANGE")
        props.function = profiling.function
        props.sort = profiling.sort
        props.output = profiling.output
