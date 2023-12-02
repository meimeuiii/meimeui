from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()
lbl = QLabel("Скільки буде 2 + 2?")
ans1 = QRadioButton("4")
ans2 = QRadioButton("14")

main_line = QVBoxLayout()
main_line.addWidget(lbl)
h2 = QHBoxLayout()
h2.addWidget(ans1)
h2.addWidget(ans2)
main_line.addLayout(h2)
def true_var_1():
    msg = QMessageBox()
    msg.setText("Правильно!")
    msg.exes()


ans1.clicked.connect(true_var_1)
window.setLayout(main_line)
window.show()
app.exec()
