from PyQt6.QtWidgets import*

app = QApplication([])
window = QWidget()
lbl = QLabel("Скільки буде 2 + 2?")
ans1 = QRadioButton("4")
ans2 = QRadioButton("14")

main_line = QVBoxLayout()
main_line.addWidget(lbl)
h1 = QHBoxLayout()


window.show()
app.exec()
