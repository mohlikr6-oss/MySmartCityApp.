import os

code = """
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

class CityServiceApp(App):
    def build(self):
        Window.clearcolor = (0.05, 0.05, 0.05, 1)
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.heading = Label(text="MY SMART CITY SERVICES", font_size='28sp', bold=True, color=(1, 0.8, 0, 1), size_hint_y=0.1)
        self.main_layout.add_widget(self.heading)
        self.info_label = Label(text="Service chunne ke liye niche click karein", font_size='18sp', color=(1, 1, 1, 1), size_hint_y=0.2, halign='center')
        self.main_layout.add_widget(self.info_label)
        scroll = ScrollView(size_hint_y=0.6)
        grid = GridLayout(cols=1, spacing=15, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        self.services_data = {
            "Plumber": "Raju Mistri\\nPhone: 9876543210\\nExp: 10 Years",
            "Electrician": "Sonu Bijli Wala\\nPhone: 9988776655\\n24/7 Service",
            "Doctor": "Dr. Verma (City Clinic)\\nPhone: 9123456789\\nTime: 10am - 8pm",
            "Grocery": "Gupta Kirana Store\\nPhone: 9000011122\\nHome Delivery Available",
            "Taxi": "Pawan Travels\\nPhone: 8888877777\\nLocal & Outstation"
        }
        for s_name in self.services_data:
            btn = Button(text=s_name, size_hint_y=None, height=120, background_color=(0, 0.5, 0.8, 1), font_size='20sp', bold=True)
            btn.bind(on_press=self.show_info)
            grid.add_widget(btn)
        scroll.add_widget(grid)
        self.main_layout.add_widget(scroll)
        self.ad_label = Button(text="--- SPONSORED AD: Click to Buy PC ---", size_hint_y=0.1, background_color=(0.2, 0.8, 0.2, 1), color=(1, 1, 1, 1))
        self.main_layout.add_widget(self.ad_label)
        return self.main_layout
    def show_info(self, instance):
        content = self.services_data[instance.text]
        self.info_label.text = f"{instance.text}\\n{content}"
        self.heading.text = "Service Details Found!"

if __name__ == '__main__':
    CityServiceApp().run()
"""

with open('main.py', 'w') as f:
    f.write(code.strip())

print("✅ main.py file kamyabi se ban gayi hai!")
