import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

#main class inherits PyQt's QMainWindow class
class Main(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)

        self.filename = ""                  #file management starts

        self.initUI()

    def initToolbar(self):
        
        #create QAction and pass it an icon and a name
        #create status tip, which displays a message in statusbar
        #create a keybpard shortcut
        #connect Qaction's triggered signal to a slot function
        
        #new, open, save, print and preview section
        self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New", self)
        self.newAction.setStatusTip("Create new document from scratch")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        self.saveAction.setStatusTip('Save document')
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
        self.printAction.setStatusTip("Print Document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.print)

        self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),"Page view",self)
        self.previewAction.setStatusTip("Preview page before printing")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)
       
        #cut, copy, paste, undo and redo section
        self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard",self)
        self.cutAction.setStatusTip("Copy text to clipboard and delete")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"),"Copy to clipboard",self)
        self.copyAction.setStatusTip("Copy text to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"),"Paste from clipboard",self)
        self.pasteAction.setStatusTip("Paste text from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"),"Undo last action",self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo"),"Redo last undone action",self)
        self.redoAction.setStatusTip("Redo last undone action")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)
        
        

        
        bulletAction = QtGui.QAction(QtGui.QIcon("icons/bullet.png"),"Insert bullet List",self)
        bulletAction.setStatusTip("Insert bullet list")
        bulletAction.setShortcut("Ctrl+Shift+B")
        bulletAction.triggered.connect(self.bulletList)
                    
        numberedAction = QtGui.QAction(QtGui.QIcon("icons/number.png"),"Insert numbered List",self)
        numberedAction.setStatusTip("Insert numbered list")
        numberedAction.setShortcut("Ctrl+Shift+L")
        numberedAction.triggered.connect(self.numberList)

        self.toolbar = self.addToolBar("Options")
        #new, open, save, print and preview section
        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)
        self.toolbar.addSeparator(
        )
        #cut, paste, undo and redo section
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)
        self.toolbar.addSeparator()

        #lists
        self.toolbar.addAction(bulletAction)
        self.toolbar.addAction(numberedAction)

        #make next toolbar appear underneath this one
        self.addToolBarBreak()

    def initFormatbar(self):
        self.formatbar = self.addToolBar("Format")

    def initMenubar(self):
        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)

        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)
        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)

    def initUI(self):
        self.text = QtGui.QTextEdit(self)
        self.setCentralWidget(self.text)
        
        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()

        #initialize statusbar on window
        self.statusbar = self.statusBar()

        #connect QTextEdit's cursorPositionChanged signal to a function
        self.text.cursorPositionChanged.connect(self.cursorPosition)

        # x and y co-oridinates i.e screen's width and height
        #setGeometry(x, y, width, height)
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("Writer")

        #show icon for window
        self.setWindowIcon(QtGui.QIcon("icons/icon.png"))

    #new() creates new instance of window and calls show() method to display it
    def  new(self):
        spawn = Main(self)
        spawn.show()
    
    def open(self):
        #show only .writer files
        #getOpenFileName() opens a dialog which returns name of file user opens
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', ".","(*.writer)")

        if self.filename:
            with open(self.filename,"rt") as file:
                self.text.setTest(file.read())

    def save(self):
        #open dialog if no filename yet
        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, 'SaveFile')

        #after having filename, check if user already entered extension when saving the file
        if not self.filename:
            self.filename = QtGui.QfileDialog.getSaveFieName(self, 'Save File')

        #just store text file contents with format in html
        #qt does this in  a nice way (or so they say)
        with open(self.filename,"wt") as file:
            file.write(self.text.toHtml())

    def print(self):
        #open printing dialog
        dialog = QtGui.QPrintDialog()

        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def preview(self):
        #open preview dialog
        preview = QtGui.QPrintPreviewDialog()
        #if print is requested, open print dialog
        preview.paintRequested.connect(lambda p:self.text.print_(p))
        preview.exec_()

    def bulletList(self):
        cursor = self.text.textCursor()
        # Insert bulleted list
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberList(self):

        cursor = self.text.textCursor()
        # Insert list with numbers
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

    #show cursor position
    def cursorPosition(self):
        cursor = self.text.textCursor()
     # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()
        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))

def main():
    app = QtGui.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
