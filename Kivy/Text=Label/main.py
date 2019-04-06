from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class TextLabel(BoxLayout):
    text_input= ObjectProperty()
    label_show= ObjectProperty()

    def txt_to_label(self):
        print(self.text_input.text)
        self.label_show.text =  self.text_input.text

    def add_to_label(self):
        self.label_show.text += "\n" + self.text_input.text

    def clearall(self):
        self.label_show.text = ""
        self.text_input.text = ""



class TextLabelApp(App):
    pass

if __name__ == '__main__':
    TextLabelApp().run()
