import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.temperature_label = QLabel("", self)
        self.emoji_label = QLabel("", self)
        self.desc_label = QLabel(self)
        self.initUi()

    def initUi(self):
        self.setFixedSize(500, 500)
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.desc_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setAlignment(Qt.AlignCenter)

        self.get_weather_button.setObjectName("get_weather_button")
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.desc_label.setObjectName("desc_label")

        self.setStyleSheet("""
            QLabel {
                font-family: calibri;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
                padding: 5px;
                
            }
            QPushButton#get_weather_button {
                font-size: 30px;
    
                padding: 10px;    
                margin: 5px;      
                background-color: lightgray;
            }
            QLabel#temperature_label {
                font-size: 70px;
            
                           
            }
            QLabel#emoji_label{
                font-family: Segoe Ui emoji;
                font-size: 100px;
            }
            QLabel#desc_label{
                font-size: 70px;               
            }
        """)
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "e2454a1db91dc0461cde60f9d9759eaa"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            print(data)

            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("bad request\nPlease check your input")

                case 401:
                    self.display_error("Unauthorized\nInvalid API key")
                case 403:
                    self.display_error(" Forbidden\nAccess denied ")

                case 404:
                    self.display_error("Not found\nCity not found")
                case 500:
                    self.display_error(
                        "Internal Server Error\nPlease try again")
                case 502:
                    self.display_error(
                        "Bad gateway\nInvalid response from server")
                case 503:
                    self.display_error("Service unavaivable\nServer is down")
                case 504:
                    self.display_error(
                        "Gateway timeout\nNo respose from server")
                case _:
                    self.display_errort(f"HTTP error ocured\n{http_error} ")

        except requests.exceptions.RequestException:
            pass

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.desc_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.desc_label.setStyleSheet("font-size: 75px;")
        weather_cond = data["weather"][0]["description"]
        self.desc_label.setText(f"{weather_cond}")

        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.weather_emoji(weather_id))

    @staticmethod
    def weather_emoji(weather_id):

        if weather_id >= 200 and weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "☁️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
