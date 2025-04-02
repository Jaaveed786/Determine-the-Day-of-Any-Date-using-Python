from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 1)  # Set background to black


def getday(date, month, year):
    month_code = {1: 0, 2: 3, 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}
    day_code = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}

    # Determine century code
    if (1600 <= year < 1700) or (2000 <= year < 2100):
        db_code = 6
    elif (1700 <= year < 1800) or (2100 <= year < 2200):
        db_code = 4
    elif (1800 <= year < 1900) or (2200 <= year < 2300):
        db_code = 2
    elif (1900 <= year < 2000):
        db_code = 0
    else:
        db_code = 0  # Default for other centuries

    yy = year % 100
    yy_quotient = yy // 4
    month_value = month_code.get(month, 0)

    total = yy + yy_quotient + date + month_value + db_code

    # Adjust for leap year (simple version)
    if (year % 4 == 0) and (month == 2):
        total -= 1

    final = total % 7
    return day_code.get(final, 'Invalid Date')


class DateCalculatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Date input fields
        self.date_input = TextInput(
            hint_text='DD',
            foreground_color=(1, 1, 1, 1),
            background_color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=40
        )
        self.month_input = TextInput(
            hint_text='MM',
            foreground_color=(1, 1, 1, 1),
            background_color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=40
        )
        self.year_input = TextInput(
            hint_text='YYYY',
            foreground_color=(1, 1, 1, 1),
            background_color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=40
        )

        # Calculate button
        calc_btn = Button(
            text='Calculate Day',
            background_color=(0, 0.5, 0.8, 1),
            size_hint_y=None,
            height=45
        )
        calc_btn.bind(on_press=self.show_day)

        # Result display
        self.result_label = Label(
            text='Day will appear here',
            color=(1, 1, 1, 1),
            font_size=20,
            bold=True
        )

        # Add widgets to layout
        layout.add_widget(Label(text='Enter Date', color=(1, 1, 1, 1)))
        layout.add_widget(self.date_input)
        layout.add_widget(self.month_input)
        layout.add_widget(self.year_input)
        layout.add_widget(calc_btn)
        layout.add_widget(self.result_label)

        return layout

    def show_day(self, instance):
        try:
            d = int(self.date_input.text)
            m = int(self.month_input.text)
            y = int(self.year_input.text)
            day = getday(d, m, y)
            self.result_label.text = f'{d}/{m}/{y} \n{day}'
        except:
            self.result_label.text = 'Invalid Input!\nPlease enter numbers'


if __name__ == '__main__':
    DateCalculatorApp().run()