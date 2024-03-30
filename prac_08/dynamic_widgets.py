from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        return self.root

    def create_labels(self):
        entries_box = self.root.ids.entries_box
        entries_box.clear_widgets()
        for name in self.names:
            label_text = f"{name}'s number is {self.name_to_phone.get(name, 'N/A')}"
            temp_label = Label(text=label_text)
            entries_box.add_widget(temp_label)

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()
        self.status_text = ""


if __name__ == "__main__":
    DynamicWidgetsApp().run()
