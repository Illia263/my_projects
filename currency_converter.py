import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


price_list = []
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.gold_label = QLabel("Enter amount of gold: ", self)
        self.gold_input = QLineEdit(self)
        self.price_label = QLabel("Enter price: ")
        self.price_input = QLineEdit(self)
        self.count_in_euros_button = QPushButton("Get price", self)
      
        self.emoji_label = QLabel("", self)
        self.desc_label = QLabel(self)
        self.initUi()

    def initUi(self):
        self.setFixedSize(1111, 600)
        vbox = QVBoxLayout()

        vbox.addWidget(self.gold_label)
        vbox.addWidget(self.gold_input)
        vbox.addWidget(self.price_label)
        vbox.addWidget(self.price_input)
        vbox.addWidget(self.count_in_euros_button)
        
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.desc_label)

        self.setLayout(vbox)

        self.gold_label.setAlignment(Qt.AlignCenter)
        self.price_label.setAlignment(Qt.AlignCenter)
        
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setAlignment(Qt.AlignCenter)

        self.count_in_euros_button.setObjectName("count_in_euros_button")
        self.gold_label.setObjectName("gold_label")
        self.gold_input.setObjectName("gold_input")
        self.price_label.setObjectName("price_label")
        self.price_input.setObjectName("price_input")
        self.emoji_label.setObjectName("emoji_label")
        self.desc_label.setObjectName("desc_label")

        self.setStyleSheet("""
            QLabel {
                font-family: calibri;
            }
            QLabel#gold_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#gold_input {
                font-size: 40px;
                padding: 5px;
                
            }
            QLabel#price_label {
                font-size: 40px;
                font-style: italic;           
            }
            QLineEdit#price_input {
                font-size: 40px;
                padding:5px;
            }
            QPushButton#count_in_euros_button {
                font-size: 30px;
    
                padding: 10px;    
                margin: 5px;      
                background-color: lightgray;
            }
            
            QLabel#emoji_label{
                font-family: Segoe Ui emoji;
                font-size: 100px;
            }
            QLabel#desc_label{
                font-size: 70px;               
            }
        """)
        self.count_in_euros_button.clicked.connect(self.calculate_priuce)
    
    def calculate_priuce(self):
        try:
            text = self.gold_input.text()
            price = self.price_input.text()
            if not text:
                return
            x = int(text)
            price_not = float(price)
            value = (x * 0.8 * 0.8) * price_not
            price_list.append(value)
            total_sum = sum(price_list)
            self.desc_label.setText(f"{total_sum:.2f} €")
            
            self.gold_input.clear()
            self.price_input.clear()
            self.emoji_label.setText("💰")
        except ValueError:
            self.desc_label.setText("Введіть число!")
            self.desc_label.setStyleSheet("color: red; font-size: 40px;")
        
        

      

   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
