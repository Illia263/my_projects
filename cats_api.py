import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

api_key = "live_GNNpOAi5hupMSLic6DdcIPb6wBeoVZwlayUhjUzRKN6wc9Ltk9Xtqa3nk7LhmN9K"
url = "https://api.thecatapi.com/v1/breeds"


class cats(QWidget):
  def __init__(self):
    super().__init__()
    self.cat_label = QLabel("Enter number of cat(1-67): ", self)
    self.cat_input = QLineEdit(self)
    self.cat_desc = QLabel(self)
    self.cat_button = QPushButton("Click to view your cat", self)
    self.initUi()

  def initUi(self):
    self.setFixedSize(800,800)
    self.cat_input.setFixedSize(500, 60)
    self.cat_desc.setWordWrap(True)
    self.cat_desc.setFixedWidth(600)
    vbox = QVBoxLayout()
    vbox.addStretch(1)
    vbox.addWidget(self.cat_label)
    vbox.addWidget(self.cat_input,alignment=Qt.AlignCenter)
    vbox.addWidget(self.cat_desc, alignment=Qt.AlignCenter)
    vbox.addWidget(self.cat_button)
    vbox.addStretch(1)
    # vbox.setSpacing(20)

    self.setLayout(vbox)

    self.cat_desc.setAlignment(Qt.AlignCenter)
    self.cat_label.setAlignment(Qt.AlignCenter)
    self.cat_input.setAlignment(Qt.AlignCenter)
    self.cat_label.setObjectName("cat_label")
    self.cat_input.setObjectName("cat_input")
    self.cat_desc.setObjectName("cat_desc")
    self.cat_button.setObjectName("cat_button")
    
    self.setStyleSheet("""
      QLabel{
        font-family: calibri;
        
      }
      QLabel#cat_desc{
        font-size: 20px;
      }
      QLabel#cat_label {
        font-size: 40px;
        font-style: italic;            
      }
      QLabel#cat_input{
        font-size: 40px;
        font-style: italic;
      }
      QPushButton#cat_button{
        font-size: 30px;
        padding: 10px;
        
        margin: 5px;
        background-color: lightgrey;
      }
    """)
    self.cat_button.clicked.connect(self.cat_logic)

  def cat_logic(self):
    text = self.cat_input.text().strip()
    headers = {
    "x-api-key" : api_key
    }
    response = requests.get(url, headers)
    if response.status_code == 200:
      data = response.json()
      
      text = self.cat_input.text()
      if not text.isdigit():
        self.cat_input.setText("Errror! Write only nums")
        return
      text = int(text)
      if not text:
        return
      if text > len(data):
        self.cat_desc.setText("Enter the number from range 1 to 67")
      cat = data[text - 1]
      if text <= len(data):
        self.cat_desc.setText(f"\n--- Your cat is ---\n Name: {cat['name']}\nCountry: {cat['origin']}\nDescription: {cat['description']}\n")
        
      else:
        self.cat_desc.setText(f"Error: {response.status_code}\n {response.text}")

     



if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = cats()
    weather_app.show()
    sys.exit(app.exec_())