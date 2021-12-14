import dearpygui.dearpygui as dpg

dpg.create_context()  # Create a context must be first thing to do to start

# Create a window
with dpg.window(label="Example Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

# how the window is displayed
dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()  # Setup DearPyGUI state manager
dpg.show_viewport()  # shows the current context

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    print("this will run every frame")
    dpg.render_dearpygui_frame()

dpg.destroy_context()  # Destroy the context is the very last thing for cleanup
