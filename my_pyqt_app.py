import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QCheckBox, QRadioButton, QComboBox, QTextEdit, QSlider, QProgressBar
from PyQt5.QtCore import Qt

class SimpleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple PyQt5 Application')
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)

        # Label
        self.label = QLabel('Hello, PyQt5!', self)
        layout.addWidget(self.label)

        # Line Edit
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText('Enter text here')
        self.line_edit.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.line_edit)

        # Button
        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        # Check Box
        self.check_box = QCheckBox('Check me', self)
        self.check_box.stateChanged.connect(self.on_check_box_changed)
        layout.addWidget(self.check_box)

        # Radio Button
        self.radio_button = QRadioButton('Select me', self)
        self.radio_button.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(self.radio_button)

        # Combo Box
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(['Option 1', 'Option 2', 'Option 3'])
        self.combo_box.currentIndexChanged.connect(self.on_combo_box_changed)
        layout.addWidget(self.combo_box)

        # Text Edit
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText('Write something here...')
        layout.addWidget(self.text_edit)

        # Slider
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.on_slider_value_changed)
        layout.addWidget(self.slider)

        # Progress Bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(50)
        layout.addWidget(self.progress_bar)

    def on_text_changed(self, text):
        self.label.setText(f'You typed: {text}')

    def on_button_click(self):
        self.label.setText('Button clicked!')

    def on_check_box_changed(self, state):
        self.label.setText(f'Check box state: {state}')

    def on_radio_button_toggled(self, checked):
        self.label.setText(f'Radio button checked: {checked}')

    def on_combo_box_changed(self, index):
        self.label.setText(f'Combo box index: {index}, value: {self.combo_box.currentText()}')

    def on_slider_value_changed(self, value):
        self.label.setText(f'Slider value: {value}')
        self.progress_bar.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleApp()
    ex.show()
    sys.exit(app.exec_())
