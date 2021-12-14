import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Tutorial"):

    # Only available if scrollX/scrollY are disabled and stretch columns are not used
    with dpg.table(header_row=False,
                   policy=dpg.mvTable_SizingFixedFit,
                   resizable=True,
                   no_host_extendX=True,
                   borders_innerV=True,
                   borders_outerV=True,
                   borders_outerH=True):

        dpg.add_table_column(label="Header 1")
        dpg.add_table_column(label="Header 2")
        dpg.add_table_column(label="Header 3")
        for i in range(0, 4):
            with dpg.table_row():
                for j in range(0, 3):
                    dpg.add_button(label=f"Row{i} Column{j} a")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
