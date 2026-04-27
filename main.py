from kivy.app import App
from kivy.ux.label import Label
import os

class MyPrankApp(App):
    def build(self):
        # هنا غادي تزيد التوكن ديال البوت ديالك ملي تخدم المساحة
        return Label(text="Ziyad Ultra AI: System Scanning...")

if __name__ == "__main__":
    MyPrankApp().run()
