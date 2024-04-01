from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class CalcGridLayout(GridLayout):
    history = []

    def calculate(self, calculation):
        if calculation:
            try:
                result = str(eval(calculation))
                self.display.text = result
                self.add_to_history(calculation, result)
            except Exception:
                self.display.text = 'Error de sintaxis'

    def add_to_history(self, expression, result):
        self.history.append(f"{expression} = {result}")
        self.update_history_label()

    def update_history_label(self):
        history_text = "\n".join(self.history)
        App.get_running_app().root.ids.history_text.text = history_text

    def borrar_historial(self):
        self.history = []
        self.update_history_label()


class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()


if __name__ == '__main__':
    CalculatorApp().run()
