from PySide6.QtWidgets import *

class mainWindow(QMainWindow):
    def setupUi(self):
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 800, 600)

        # Crear la ventana principal y establecer un widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Crear un diseño vertical para el widget central
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Agregar un QLabel al diseño
        label = QLabel("Hello, World!")
        layout.addWidget(label)

import sys
app = QApplication(sys.argv)
window = mainWindow()
window.setupUi()
window.show()

sys.exit(app.exec_())