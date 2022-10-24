try:
    from PySide6.QtCore import *
    from PySide6.QtUiTools import *
    from PySide6.QtGui import *
    from PySide6.QtWidgets import *
except:
    from PyQt5.QtCore import *
    from PyQt5.QtUiTools import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *

from functools import partial




def clear_layout(layout):
    """
    Clears a layout of all widgets in it
    #https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt

    :param layout: <QLayout>
    :return: None
    """
    if layout is not None:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clear_layout(child.layout())


def delete_window(object=None, name=None):
    """
    Deletes a a window. Pass in either the object or the object name

    :param object: <QObject> you want to delete
    :param name: <string> objectName of the object you want to delete
    :param delete_later: <bool>
    :return:
    """
    app = QApplication.instance()
    for widget in app.topLevelWidgets():
        if object is not None:
            if str(widget.__class__) == str(object.__class__):
                widget.deleteLater()
                widget.close()

        elif name is not None:
            if str(widget.__class__) == name:
                widget.deleteLater()
                widget.close()

def blur_widget(widget, including_children=True, radius=10):
    """
    Blurs a QWidget

    :param widget: <QWidget>
    :param including_children: <bool> self exaplanatory
    :param radius: <int> how much blurriness you want
    :return:
    """
    blur = QGraphicsBlurEffect()
    blur.setBlurRadius(radius)

    widget.setGraphicsEffect(blur)

    if including_children:
        for child in widget.findChildren(QWidget):
            try:
                print(child)
                child.setGraphicsEffect(blur)
            except:
                print("can't do it!")
                pass

class QHLine(QFrame):
    def __init__(self):
        """
        Adds a horizontal line, like you can do in QtDesigner

        """
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)


class QVLine(QFrame):
    def __init__(self):
        """
        Adds a horizontal line, like you can do in QtDesigner

        """
        super(QVLine, self).__init__()
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)



def clickable(widget):
    """
    Makes a QWidget that's not clickable, clickable anyway :)
    # https://wiki.python.org/moin/PyQt/Making%20non-clickable%20widgets%20clickable

    use:
    my_label = QLabel("Click me!")
    clickable(my_label).connect(identify)

    def identify():
        print("Got clicked!")

    :param widget: <QWidget> you want to make clickable
    :return:
    """
    class Filter(QObject):
        clicked = Signal()
        dropped = Signal()

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        if event.button() == Qt.LeftButton:
                            self.clicked.emit()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


def get_all_widgets_in_layout(layout):
    """
    Recursively gets all the items of a layout

    :param layout: <QLayout>
    :return:
    """

    def get_children(item):
        try:
            for index in range(item.count()):
                yield item.itemAt(index).widget()

                for index_2 in get_children(item.itemAt(index)):
                    yield index_2
        except:
            pass

    children = get_children(layout)
    return [child for child in children if child is not None]



class LineEditWithClearButton(QLineEdit):
    """
    QLineEdit with a X button at the end
    #https://stackoverflow.com/a/12468386

    """
    def __init__(self, parent=None):
        super(LineEditWithClearButton, self).__init__(parent)

        self.clear_button = QToolButton(self)

        self.clear_button.setIcon(self.style().standardIcon(getattr(QStyle, "SP_DialogCancelButton")))

        self.clear_button.setStyleSheet('border: 0px; padding: 0px;')
        self.clear_button.setCursor(Qt.PointingHandCursor)
        self.clear_button.clicked.connect(self.clear)

        frame_width = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)
        button_size = self.clear_button.sizeHint()

        self.setStyleSheet('QLineEdit {padding-right: %dpx; }' % (button_size.width() + frame_width + 1))
        self.setMinimumSize(max(self.minimumSizeHint().width(), button_size.width() + frame_width*2 + 2),
                            max(self.minimumSizeHint().height(), button_size.height() + frame_width*2 + 2))

        self.textChanged.connect(self.check_clear_button_enabled)
        self.check_clear_button_enabled()

    def check_clear_button_enabled(self):
        if self.text():
            self.clear_button.setEnabled(True)
        else:
            self.clear_button.setEnabled(False)

    def resizeEvent(self, event):
        button_size = self.clear_button.sizeHint()
        frame_width = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth)
        self.clear_button.move(self.rect().right() - frame_width - button_size.width(), (self.rect().bottom() - button_size.height() + 3)/2)
        super(LineEditWithClearButton, self).resizeEvent(event)


class EasyUI(QMainWindow):
    def __init__(self, window_title="Easy UI Window", horizontal_layout=False, vertical_layout=True, parent=None):
        """
        Make a QtMainwindow that you easily can add buttons to. Helpful if you want to make a quick tool without
        having to code a window from scratch or use a .ui file

        :param window_title: <string> optional window title
        :param: horizontal_layout: <bool> set to True to have to buttons horizontal
        :param: vertical_layout: <bool> True by default, puts the buttons underneath eachother
        :param parent: <QMainWindow> like Maya's main window
        """
        super(EasyUI, self).__init__(parent)

        self.central_widget = QWidget(self)

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle(window_title)
        self.setObjectName(filter(str.isalpha, window_title))

        if horizontal_layout is True:
            self.horizontal_layout = QHBoxLayout(self.central_widget)
            self.layout = self.horizontal_layout
        else:
            self.vertical_layout = QVBoxLayout(self.central_widget)
            self.layout = self.vertical_layout

    def add_button(self, caption, command, *args, **kwargs):
        """
        Adds a button to the window

        :param caption: Text on the button
        :param command: Function that needs to be called
        :param tooltip: tooltip to add to the button
        :param height: fixed height of the button
        :return: The button that was created


        Example:
        def print_something(mandatory, **kwargs):
            print mandatory
            for key, value in kwargs.iteritems():
                if key == "optional":
                    if value != "":
                        print value

        def print_whaa():
            print "whaa"

        ez_win = qutils.EasyUI(window_title="My super tool!", horizontal_layout=True)
        ez_win.add_button("Print Something Button", print_something, "this is the mandatory message", button_tooltip="this is the tip of the tool", message="this is the message")
        ez_win.add_button("Print Whaa Button", print_whaa, button_height=25)
        ez_win.show()


        """
        if caption is None or command is None:
            raise RuntimeError("Caption or command have to be set!")

        tooltip = kwargs.get("button_tooltip")
        height = kwargs.get("button_height")

        button = QPushButton(self)
        button.setText(caption)
        if not kwargs:
            button.clicked.connect(command)
        else:
            button.clicked.connect(partial(command, *args, **kwargs))
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        if tooltip:
            button.setToolTip(tooltip)

        if height:
            button.setFixedHeight(height)

        self.layout.addWidget(button)

        return button

    def add_generic_widget(self, widget):
        self.layout.addWidget(widget)

    def show_ui(self):
        """
        Shows the window

        :return:
        """
        self.show()

def get_named_parent_widget(source_widget, parent_widget_object_name):
    """
    Returns the parent widget with a given name of source_widget

    :param source_widget: <QWidget>
    :param parent_widget_object_name: <string> objectName of the parent widget you're looking for
    :return:
    """
    parent_widget = source_widget.parentWidget()
    if parent_widget is not None and parent_widget.objectName() != parent_widget_object_name:
        return get_named_parent_widget(parent_widget, parent_widget_object_name)
    return parent_widget

