from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLineEdit,
    QLabel) 

from PyQt5 import QtGui
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


styles_for_btn = """
    QPushButton {
        color: black;
        border: 1px solid black;
        font-weight: 600;
    }
    QPushButton:hover {
        color: grey;
        border: 1px solid; 
        font-weight: 700;
    }
    QPushButton::focus {
        color: grey;
        border-color: black;
        font-size: 10px;
    }
    """

def rubles_to_dollars(input_rubles, result_container):
    ru_count = float(input_rubles.text())
    result = str(ru_count/80.0) + "$"
    result_container.setText(result)

def dollars_to_rubles(input_rubles, result_container):
    dol_count = float(input_rubles.text())
    result = str(dol_count*80.0) + "p"
    result_container.setText(result)

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
label_info = QLabel("")
window.setStyleSheet("color:black;")
window.setWindowTitle("Конвертатор валют")

result_container = QLabel()
input_rubles = QLineEdit()
input_rubles.setPlaceholderText("Введите рубли")
input_dollars = QLineEdit()
input_dollars.setPlaceholderText("Введите доллары")
window.setWindowIcon(QtGui.QIcon(''))

btn_rubles = QPushButton("Перевести рубли\n в доллары")
btn_rubles.clicked.connect(
    lambda: rubles_to_dollars(input_rubles, result_container)
)

btn_dollars = QPushButton("Перевести\nдоллары в рубли")
btn_dollars.clicked.connect(
    lambda: dollars_to_rubles(input_rubles, result_container)
)

h_layout1 = QHBoxLayout()
h_layout1.addWidget(input_rubles)
h_layout1.addWidget(btn_rubles)
h_layout2 = QHBoxLayout()
h_layout2.addWidget(input_dollars)
h_layout2.addWidget(btn_dollars)
layout.addLayout(h_layout1)
layout.addLayout(h_layout2)
layout.addWidget(result_container)


window.setLayout(layout)
window.resize(350, 0)
window.show()
app.exec_()
