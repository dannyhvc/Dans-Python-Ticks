import dearpygui.dearpygui as dpg


def gui_start() -> None:
    dpg.create_context()

    with dpg.window(label="Main", tag="main_window") as main_window:
        with dpg.menu_bar():
            with dpg.menu(label="Themes"):
                dpg.add_menu_item(label="Dark")
                dpg.add_menu_item(label="Light")
                dpg.add_menu_item(label="Classic")

                with dpg.menu(label="Other Themes"):
                    dpg.add_menu_item(label="Purple")
                    dpg.add_menu_item(label="Gold")
                    dpg.add_menu_item(label="Red")

            with dpg.menu(label="Tools"):
                dpg.add_menu_item(label="Show Logger")
                dpg.add_menu_item(label="Show About")

            with dpg.menu(label="Oddities"):
                dpg.add_button(label="A Button")
                dpg.add_simple_plot(label="Menu plot", default_value=(
                    0.3, 0.9, 2.5, 8.9), height=80)

    with dpg.window(label="DearPyGui"):
        with dpg.group(label="Group0", horizontal=True, tag="group0"):
            dpg.add_button(label="Button1")
            dpg.add_button(label="Button2")

        with dpg.group(label="Group1", horizontal=True, tag="group1"):
            dpg.add_button(label="Button3")
            dpg.add_button(label="Button4")
            dpg.add_button(label="Button5")

        with dpg.group(label="Group2", horizontal=True, tag="group2"):
            dpg.add_button(label="Button6")
            dpg.add_button(label="Button7")

        with dpg.group(label="Group3", horizontal=True, tag="group3"):
            with dpg.menu(label="Themes"):
                dpg.add_menu_item(label="Dark")
                dpg.add_menu_item(label="Light")

        with dpg.group(label="Group4", horizontal=True, tag="group4"):

            dpg.add_button(label="Button8")
            dpg.add_button(label="Button9")
            dpg.add_button(label="Button10")

    dpg.create_viewport(title='Custom Title', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("main_window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


def main():
    gui_start()


if __name__ == '__main__':
    main()
