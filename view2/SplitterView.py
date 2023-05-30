from PyQt5.QtWidgets import QComboBox, QPushButton, QDialog
from PyQt5 import uic


class SplitterView(QDialog):

    output_file :str

    def __init__(self, input_file :dict, widget):
        super(SplitterView, self).__init__()
        # Leer la UI
        uic.loadUi('./view2/interface/formatter.ui', self)

        # Definir componentes
        self.splitter_input = self.findChild(QComboBox, 'splitter_input')
        self.button_next = self.findChild(QPushButton, 'siguiente')
        
        # Añadir contenido al componentes
        self.add_content(self.splitter_input, "splitter", input_file)
        self.button_next.clicked.connect(lambda: self.on_submit(input_file, widget))
        
        # Mostrar la app
        self.show()



    def add_content(self, element :object, key, input_file):
        for content in input_file[key]:
            element.addItem(content)



    def on_submit(self, input_file, widget):
        # Obtener el contenido del Combo Box 
        splitter_data = self.splitter_input.currentText()

        # Preparar la ventana
        window = FileInformation(input_file, widget)
        width = 555
        height = 500

        # Abrir la seguiente ventana
        self.open_window(window, widget,  width, height)
        
        return self.content


    
    def open_window(self, window, widget, width, height):
        try:
            widget.addWidget(window)
            widget.setFixedWidth(width)
            widget.setFixedHeight(height)
            widget.setCurrentIndex(widget.currentIndex()+1)
            return True
        except:
            return False


