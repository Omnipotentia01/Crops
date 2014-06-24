import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        #instantiate layout and widget for layout to go in
        self.stacked_layout = QStackedLayout()
        self.stacked_widget = QWidget()
        #set layout of stacked widget
        self.stacked_widget.setLayout(self.stacked_layout)
        #create layouts
        self.create_main_layout()
        self.create_hello_layout()
        #create central widget
        self.setCentralWidget(self.stacked_widget)
        #set the initial layout
        self.stacked_layout.setCurrentIndex(0)
        self.submit_button.setFocus()

    def create_main_layout(self):
        #components/widgets
        self.text_box = QLineEdit()
        self.text_box.setPlaceholderText("Enter your name: ")
        self.submit_button = QPushButton("Submit")
        #create layout
        self.initial_layout = QVBoxLayout()
        #add widgets to layout
        self.initial_layout.addWidget(self.text_box)
        self.initial_layout.addWidget(self.submit_button)
        #create widget to hold layout
        self.initial_widget = QWidget()
        #add layout to the widget
        self.initial_widget.setLayout(self.initial_layout)
        #Add initial_widget (with initail layout attached) to stacked layout
        self.stacked_layout.addWidget(self.initial_widget)
        #connections
        self.submit_button.clicked.connect(self.switch_to_hello_layout) #Button clicked
        self.text_box.returnPressed.connect(self.switch_to_hello_layout) #Enter key pressed

    def create_hello_layout(self):
        #components        
        self.label = QLabel()
        self.back_button = QPushButton("Back")

        self.hello_layout = QVBoxLayout()
        
        self.hello_layout.addWidget(self.label)
        self.hello_layout.addWidget(self.back_button)
        #create widget to hold layout
        self.hello_widget = QWidget()
        #add layout to the widget
        self.hello_widget.setLayout(self.hello_layout)
        #Add hello_widget (with hello_layout attached) to stacked layout
        self.stacked_layout.addWidget(self.hello_widget)
        #connections
        self.back_button.clicked.connect(self.switch_to_initial_layout) #Button clicked

    def switch_to_hello_layout(self):
        self.stacked_layout.setCurrentIndex(1)
        name = self.text_box.text()
        self.label.setText("Hello {0}!".format(name))
        
    def switch_to_initial_layout(self):
        self.stacked_layout.setCurrentIndex(0)
        self.text_box.clear()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
    
