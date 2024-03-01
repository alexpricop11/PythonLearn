from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from googletrans import LANGUAGES, Translator


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.layout = None
        self.calc_input = None
        self.translator = Translator()

    def build(self):
        self.title = "Translate Calculator"
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.main_menu()

        return self.layout

    def main_menu(self):
        self.layout.clear_widgets()
        options = Label(text="Alege o optiune", font_size=40, size_hint_y=None, height=50)
        options.color = (0, 1, 0, 1)
        self.layout.add_widget(options)
        buttons_layout = BoxLayout(orientation='horizontal', spacing=5)
        btn_translate = Button(text='Traducator', font_size=70, size_hint=(.7, .9))
        btn_translate.bind(on_press=self.show_translator)
        btn_calculator = Button(text='Calculator', font_size=70, size_hint=(.7, .9))
        btn_calculator.bind(on_press=self.show_calculator)
        buttons_layout.add_widget(btn_translate)
        buttons_layout.add_widget(btn_calculator)
        self.layout.add_widget(buttons_layout)

    def show_translator(self, instance):
        if not instance.get_parent_window():
            return  # Dacă widgetul nu are fereastră părinte, este ascuns

        translator_popup = DropDown()

        def on_select(btn):
            self.translate_text(btn.text)

        for language_code, language_name in LANGUAGES.items():
            btn = Button(text=language_name, size_hint_y=None, height=44)
            btn.bind(on_release=on_select)
            translator_popup.add_widget(btn)

        if not translator_popup.attach_to:
            # Dacă lista dropdown nu este deja deschisă, deschide-o
            translator_popup.open(instance)
        else:
            # Dacă lista dropdown este deja deschisă, închide-o
            translator_popup.dismiss()

    def translate_text(self, language_name):
        try:
            translated_text = self.translator.translate("Ai ales opțiunea traducător", dest=language_name)
            self.layout.clear_widgets()
            translated_label = Label(text=translated_text.text)
            back_button = Button(text="Înapoi", size_hint=(.2, .1))
            back_button.bind(on_press=self.main_menu)
            self.layout.add_widget(back_button)
            self.layout.add_widget(translated_label)
        except Exception as e:
            error_label = Label(text="Eroare la traducere")
            back_button = Button(text="Înapoi", size_hint=(.2, .1))
            back_button.bind(on_press=self.main_menu)
            self.layout.add_widget(back_button)
            self.layout.add_widget(error_label)

    def show_calculator(self, instance):
        self.layout.clear_widgets()
        self.calc_input = TextInput(text='', multiline=False)
        calc_button = Button(text="Calculează", size_hint=(.2, .1))
        calc_button.bind(on_press=self.calculate)
        back_button = Button(text="Înapoi", size_hint=(.2, .1))
        back_button.bind(on_press=self.main_menu)
        self.layout.add_widget(self.calc_input)
        self.layout.add_widget(calc_button)
        self.layout.add_widget(back_button)

    def calculate(self, instance):
        try:
            result = eval(self.calc_input.text)
            self.layout.add_widget(Label(text=str(result)))
        except Exception as error:
            self.layout.add_widget(Label(text="Eroare la calcul"))


if __name__ == '__main__':
    MyApp().run()
