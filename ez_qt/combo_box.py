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

def add_items(combo_box, items, duplicates_allowed=False, clear=False, string_split_character=None):
    """
    Convenience function to add items to a combobox

    :param combo_box: your QComboBox
    :param items: <string> | <list> a single string item ("option"), a list (["option_1", "option_2"]), or a string that can be split on a character like a comma separated string ("option_1, option_2")
    :param duplicates_allowed: <bool> whether or not allow duplicates in the combobox
    :param clear: <bool> clear the comboBox before adding stuff
    :param string_split_character: <string> split the string on this character (eg: ","), the result is the list of items that get added to the combobox
    :return:
    """
    if not isinstance(items, (list, tuple)):
        if isinstance(items, str) and string_split_character is not None and string_split_character in items:
            tmp_list = [part.strip() for part in items.split(string_split_character)]
            items = tmp_list
        elif isinstance(items, str) and items == "":
            return
        else:
            items = [items]

    if clear is True:
        combo_box.clear()

    for item in items:
        if duplicates_allowed is True:
            combo_box.addItem(item)
        else:
            if combo_box.findText(item, Qt.MatchExactly) == -1 and item is not None:
                combo_box.addItem(item)


def remove_items(combo_box, items, string_split_character=None):
    """
    Convenience function to remove items from a combo box

    :param combo_box: your QComboBox
    :param items: <string> | <list> a single string item ("option"), a list (["option_1", "option_2"]), or a string that can be split on a character like a comma separated string ("option_1, option_2")
    :param string_split_character: <string> split the string on this character (eg: ","), the result is the list of items that get added to the combobox
    :return:
    """
    if not isinstance(items, (list, tuple)):
        if isinstance(items, str) and string_split_character is not None and string_split_character in items:
            tmpList = [part.strip() for part in items.split(string_split_character)]
            items = tmpList
        else:
            items = [items]

    for item in items:
        index = combo_box.findText(item, Qt.MatchExactly)
        if index != -1:
            combo_box.removeItem(index)


def set_to_item(combo_box, item_text, reload=False):
    """
    Convenience function to set the text of a combobox to a certain item of the combobox

    :param combo_box: your QComboBox
    :param item_text: <string> text you're looking for
    :param reload: <bool> if True will reload the combobox, even if the text you're setting it to is the current text
    :return:
    """
    if reload is True:
        combo_box.setCurrentIndex(-1)

    index = combo_box.findText(item_text, Qt.MatchExactly)
    if index != -1:
        combo_box.setCurrentIndex(index)
    else:
        raise ValueError("%s is not an item in %s" % (item_text, combo_box.objectName()))


def get_all_items(combo_box):
    """
    Gets all the items in a combobox as a list. Will raise an IndexError if there are not

    items in the combobox
    :param combo_box: your QComboBox
    :return: items of the QComboBox
    """
    items = []
    for item in [combo_box.itemText(i) for i in
                 range(combo_box.count())]:
        if item is not None:
            items.append(item)

    return items