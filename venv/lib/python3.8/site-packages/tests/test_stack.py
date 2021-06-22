import pytest
from pytestqt.plugin import qt_api

from PyQt5.QtCore import Qt
from app import MainWindow

def test_basics(qtbot):
    """
    Basic test that works more like a sanity check to ensure we are setting up a QApplication
    properly and are able to display a simple event_recorder.
    """
    assert qt_api.QApplication.instance() is not None
    widget = qt_api.QWidget()
    qtbot.addWidget(widget)
    widget.setWindowTitle("W1")
    widget.show()

    assert widget.isVisible()
    assert widget.windowTitle() == "W1"

#def test_shape(qtbot):
#    window = MainWindow()
#    window.show()
#    qtbot.addWidget(window)

    #qtbot.mouseClick(window, Qt.LeftButton)
    #window.load_images(fpath="/Users/edluffy/Documents/breadboard/images")

