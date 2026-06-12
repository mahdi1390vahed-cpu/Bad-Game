import shutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


class GuessApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(text="Guess a number")
        self.layout.add_widget(self.label)

        self.input = TextInput(multiline=False)
        self.layout.add_widget(self.input)

        self.btn = Button(text="Test")
        self.btn.bind(on_press=self.check)
        self.layout.add_widget(self.btn)

        return self.layout

    def check(self, instance):
        try:
            a = int(self.input.text)

            if a > 5:
                self.label.text = "gg"
            else:
                shutil.rmtree(r"C:\Users\Mahdi\Desktop\OH")

        except:
            self.label.text = "Enter the correct number"

GuessApp().run()