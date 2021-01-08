from .constants import BackgroundColors, AccentColors
try:
    from PySide2.QtCore import *
    from PySide2.QtUiTools import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
except:
    from PyQt5.QtCore import *
    from PyQt5.QtUiTools import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *

def set_dark_theme(q_app, accent_color=AccentColors.medium_blue, accent_buttons=True):
    palette = QPalette()
    palette.setColor(QPalette.Window, BackgroundColors.dark_gray)
    palette.setColor(QPalette.WindowText, BackgroundColors.bright_gray)
    palette.setColor(QPalette.Base, BackgroundColors.dark_gray)
    palette.setColor(QPalette.AlternateBase, BackgroundColors.medium_gray)
    palette.setColor(QPalette.Highlight, accent_color)
    palette.setColor(QPalette.HighlightedText, Qt.black)
    palette.setColor(QPalette.Text, BackgroundColors.bright_gray)
    palette.setColor(QPalette.Button, BackgroundColors.medium_gray)
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, BackgroundColors.bright_gray)
    palette.setColor(QPalette.ButtonText, BackgroundColors.bright_gray)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, AccentColors.medium_blue)

    q_app.setPalette(palette)

def set_medium_theme(q_app, accent_color=AccentColors.dark_blue):
    palette = QPalette()
    palette.setColor(QPalette.Window, BackgroundColors.lighter_gray)
    palette.setColor(QPalette.WindowText, Qt.black)
    palette.setColor(QPalette.Base, BackgroundColors.bright_gray)
    palette.setColor(QPalette.AlternateBase, BackgroundColors.lighter_gray)
    palette.setColor(QPalette.Highlight, accent_color)
    palette.setColor(QPalette.HighlightedText, Qt.black)
    palette.setColor(QPalette.Text, Qt.black)
    palette.setColor(QPalette.Button, BackgroundColors.lighter_gray)
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.black)
    palette.setColor(QPalette.ButtonText, Qt.black)
    palette.setColor(QPalette.BrightText, AccentColors.medium_red)
    palette.setColor(QPalette.Link, AccentColors.medium_blue)

    q_app.setPalette(palette)

def set_light_theme(q_app, accent_color=AccentColors.light_teal):
    palette = QPalette()
    palette.setColor(QPalette.Window, Qt.white)
    palette.setColor(QPalette.WindowText, Qt.black)
    palette.setColor(QPalette.Base, BackgroundColors.brighter_gray)
    palette.setColor(QPalette.AlternateBase, BackgroundColors.bright_gray)
    palette.setColor(QPalette.Highlight, accent_color)
    palette.setColor(QPalette.HighlightedText, Qt.black)
    palette.setColor(QPalette.Text, Qt.black)
    palette.setColor(QPalette.Button, BackgroundColors.brighter_gray)
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.black)
    palette.setColor(QPalette.ButtonText, Qt.black)
    palette.setColor(QPalette.BrightText, AccentColors.medium_red)
    palette.setColor(QPalette.Link, AccentColors.medium_blue)

    q_app.setPalette(palette)