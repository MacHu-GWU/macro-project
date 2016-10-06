#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
bot is this mouse and keyboard simulation module, built on top of
PyUserInput/pymouse/pykeyboard/pywin32/pyperclip.
"""

import sys
import time
import string

try:
    from pymouse import PyMouse
    from pykeyboard import PyKeyboard
except ImportError as e:
    raise ImportError("please install PyUserInput!")

try:
    import pyperclip
except ImportError as e:
    raise ImportError("please install pyperclip!")


class Bot(object):

    """Mouse and Keyboard robot class.

    Abbreviation table:

    - m: stands for mouse
    - k: stands for keyboard
    - dl: stands for delay
    - n: how many times you want to tap the key
    - i: usually for the ith function key, F1 ~ F12

    Almost every method have an option keyword ``dl`` (dl stands for delay), there
    is ``dl`` seconds delay applied at begin. By default it is ``None``, means no
    delay applied.
    
    Keyboard Key Name Table (Case Insensitive)::
    
        # Main Keyboard Keys
        "ctrl": self.k.control_key,
        "l_ctrl": self.k.control_l_key,
        "r_ctrl": self.k.control_r_key,
        "alt": self.k.alt_key,
        "l_alt": self.k.alt_l_key,
        "r_alt": self.k.alt_r_key,
        "shift": self.k.shift_key,
        "l_shift": self.k.shift_l_key,
        "r_shift": self.k.shift_r_key,
        "tab": self.k.tab_key,
        "space": self.k.space_key,
        "enter": self.k.enter_key,
        "back": self.k.backspace_key,
        "backspace": self.k.backspace_key,

        # Side Keyboard Keys
        "home": self.k.home_key,
        "end": self.k.end_key,
        "page_up": self.k.page_up_key,
        "pageup": self.k.page_up_key,
        "page_down": self.k.page_down_key,
        "page_down": self.k.page_down_key,
        "insert": self.k.insert_key,
        "ins": self.k.insert_key,
        "delete": self.k.delete_key,
        "del": self.k.delete_key,

        "up": self.k.up_key,
        "down": self.k.down_key,
        "left": self.k.left_key,
        "right": self.k.right_key,
        
        # Function Keys
        "f1": F1        
    """

    def __init__(self):
        self.m = PyMouse()
        self.k = PyKeyboard()
        self.dl = 0

        self._key_mapper = {
            # Main Keyboard Keys
            "ctrl": self.k.control_key,
            "l_ctrl": self.k.control_l_key,
            "r_ctrl": self.k.control_r_key,
            "alt": self.k.alt_key,
            "l_alt": self.k.alt_l_key,
            "r_alt": self.k.alt_r_key,
            "shift": self.k.shift_key,
            "l_shift": self.k.shift_l_key,
            "r_shift": self.k.shift_r_key,
            "tab": self.k.tab_key,
            "space": self.k.space_key,
            "enter": self.k.enter_key,
            "back": self.k.backspace_key,
            "backspace": self.k.backspace_key,

            # Side Keyboard Keys
            "home": self.k.home_key,
            "end": self.k.end_key,
            "page_up": self.k.page_up_key,
            "pageup": self.k.page_up_key,
            "page_down": self.k.page_down_key,
            "page_down": self.k.page_down_key,
            "insert": self.k.insert_key,
            "ins": self.k.insert_key,
            "delete": self.k.delete_key,
            "del": self.k.delete_key,

            "up": self.k.up_key,
            "down": self.k.down_key,
            "left": self.k.left_key,
            "right": self.k.right_key,

            # f1 - f12 is the function key
        }
        for i in range(1, 1+12):
            self._key_mapper["f%s" % i] = self.k.function_keys[i]

    def _parse_key(self, name):
        name = str(name)
        if name in string.printable:
            return name
        elif name.lower() in self._key_mapper:
            return self._key_mapper[name.lower()]
        else:
            raise ValueError(
                "%r is not a valid key name, use one of %s." % (name, list(self._key_mapper)))

    def delay(self, dl=0):
        """Delay for ``dl`` seconds.
        """
        if dl is None:
            time.sleep(self.dl)
        elif dl < 0:
            sys.stderr.write(
                "delay cannot less than zero, this takes no effects.\n")
        else:
            time.sleep(dl)

    #--- Meta ---
    def get_screen_size(self):
        """Return screen's width and height in pixel.

        **中文文档**

        返回屏幕的像素尺寸。
        """
        width, height = self.m.screen_size()
        return width, height

    def get_position(self):
        """Return the current coordinate of mouse.

        **中文文档**

        返回鼠标所处的位置坐标。
        """
        x_axis, y_axis = self.m.position()
        return x_axis, y_axis

    #--- Mouse Macro ---
    def left_click(self, x, y, n=1, pre_dl=None, post_dl=None):
        """Left click at ``(x, y)`` on screen for ``n`` times.
        at begin.

        **中文文档**

        在屏幕的 ``(x, y)`` 坐标处左键单击 ``n`` 次。
        """
        self.delay(pre_dl)
        self.m.click(x, y, 1, n)
        self.delay(post_dl)
        
    def right_click(self, x, y, n=1, pre_dl=None, post_dl=None):
        """Right click at ``(x, y)`` on screen for ``n`` times.
        at begin.

        **中文文档**

        在屏幕的 ``(x, y)`` 坐标处右键单击 ``n`` 次。
        """
        self.delay(pre_dl)
        self.m.click(x, y, 2, n)
        self.delay(post_dl)

    def middle_click(self, x, y, n=1, pre_dl=None, post_dl=None):
        """Middle click at ``(x, y)`` on screen for ``n`` times.
        at begin.

        **中文文档**

        在屏幕的 ``(x, y)`` 坐标处中键单击 ``n`` 次。
        """
        self.delay(pre_dl)
        self.m.click(x, y, 3, n)
        self.delay(post_dl)

    def scroll_up(self, n, pre_dl=None, post_dl=None):
        """Scroll up ``n`` times.

        **中文文档**

        鼠标滚轮向上滚动n次。
        """
        self.delay(pre_dl)
        self.m.scroll(vertical=n)
        self.delay(post_dl)

    def scroll_down(self, n, pre_dl=None, post_dl=None):
        """Scroll down ``n`` times.

        **中文文档**

        鼠标滚轮向下滚动n次。
        """
        self.delay(pre_dl)
        self.m.scroll(vertical=-n)
        self.delay(post_dl)

    def scroll_right(self, n, pre_dl=None, post_dl=None):
        """Scroll right ``n`` times.

        **中文文档**

        鼠标滚轮向右滚动n次(如果可能的话)。
        """
        self.delay(pre_dl)
        self.m.scroll(horizontal=n)
        self.delay(post_dl)

    def scroll_left(self, n, pre_dl=None, post_dl=None):
        """Scroll left ``n`` times.

        **中文文档**

        鼠标滚轮向左滚动n次(如果可能的话)。
        """
        self.delay(pre_dl)
        self.m.scroll(horizontal=-n)
        self.delay(post_dl)

    def move_to(self, x, y, pre_dl=None, post_dl=None):
        """Move mouse to (x, y)

        **中文文档**

        移动鼠标到 (x, y) 的坐标处。
        """
        self.delay(pre_dl)
        self.m.move(x, y)
        self.delay(post_dl)

    def drag_and_release(self, start_x, start_y, end_x, end_y, pre_dl=None, post_dl=None):
        """Drag something from (start_x, start_y) to (end_x, endy)

        **中文文档**

        从start的坐标处鼠标左键单击拖曳到end的坐标处
        start, end是tuple. 格式是(x, y)
        """
        self.delay(pre_dl)
        self.m.press(start_x, start_y, 1)
        self.m.drag(end_x, end_y)
        self.m.release(end_x, end_y, 1)
        self.delay(post_dl)

    #--- Keyboard Single Key ---
    def tap_key(self, key_name, n=1, interval=0, pre_dl=None, post_dl=None):
        """Tap a key on keyboard for ``n`` times, with ``interval`` seconds of
        interval. Key is declared by it's name

        Example::

            bot.tap_key("a")
            bot.tap_key(1)
            bot.tap_key("up")
            bot.tap_key("space")
            bot.tap_key("enter")
            bot.tap_key("tab")

        **中文文档**

        以 ``interval`` 中定义的频率按下某个按键 ``n`` 次。接受按键名作为输入。
        """
        key = self._parse_key(key_name)
        self.delay(pre_dl)
        self.k.tap_key(key, n, interval)
        self.delay(post_dl)

    def enter(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Press enter key n times.

        **中文文档**

        按回车键/换行键 n 次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.enter_key, n, interval)
        self.delay(post_dl)

    def backspace(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Press backspace key n times.

        **中文文档**

        按退格键 n 次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.backspace_key, n, interval)
        self.delay(post_dl)

    def space(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Press white space key n times.

        **中文文档**

        按空格键 n 次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.space_key, n)
        self.delay(post_dl)

    def fn(self, i, n=1, interval=0, pre_dl=None, post_dl=None):
        """Press Fn key n times.

        **中文文档**

        按 Fn 功能键 n 次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.function_keys[i], n, interval)
        self.delay(post_dl)

    def tab(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Tap ``tab`` key for ``n`` times, with ``interval`` seconds of interval.

        **中文文档**

        以 ``interval`` 中定义的频率按下某个tab键 ``n`` 次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.tab_key, n, interval)
        self.delay(post_dl)

    def up(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Press up key n times.

        **中文文档**

        按上方向键 n 次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.up_key, n, interval)
        self.delay(post_dl)

    def down(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Press down key n times.

        **中文文档**

        按下方向键 n 次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.down_key, n, interval)
        self.delay(post_dl)

    def left(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Press left key n times

        **中文文档**

        按左方向键 n 次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.left_key, n, interval)
        self.delay(post_dl)

    def right(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Press right key n times.

        **中文文档**

        按右方向键 n 次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.right_key, n, interval)
        self.delay(post_dl)

    def delete(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Pres delete key n times.

        **中文文档**

        按 delete 键n次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.delete_key, n, interval)
        self.delay(post_dl)

    def insert(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Pres insert key n times.

        **中文文档**

        按 insert 键n次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.insert_key, n, interval)
        self.delay(post_dl)

    def home(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Pres home key n times.

        **中文文档**

        按 home 键n次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.home_key, n, interval)
        self.delay(post_dl)

    def end(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Press end key n times.

        **中文文档**

        按 end 键n次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.end_key, n, interval)
        self.delay(post_dl)

    def page_up(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Pres page_up key n times.

        **中文文档**

        按 page_up 键n次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.page_up_key, n, interval)
        self.delay(post_dl)

    def page_down(self, n=1, interval=0, pre_dl=None, post_dl=None):
        """Pres page_down key n times.

        **中文文档**

        按 page_down 键n次。
        """
        self.delay(pre_dl)
        self.k.tap_key(self.k.page_down, n, interval)
        self.delay(post_dl)

    #--- Keyboard Combination ---
    def press_and_tap(self, press_key, tap_key, n=1, interval=0, pre_dl=None, post_dl=None):
        """Press combination of two keys, like Ctrl + C, Alt + F4. The second
        key could be tapped for multiple time.

        Examples::

            bot.press_and_tap("ctrl", "c")
            bot.press_and_tap("shift", "1")

        **中文文档**

        按下两个键的组合键。
        """
        press_key = self._parse_key(press_key)
        tap_key = self._parse_key(tap_key)

        self.delay(pre_dl)
        self.k.press_key(press_key)
        self.k.tap_key(tap_key, n, interval)
        self.k.release_key(press_key)
        self.delay(post_dl)

    def press_two_and_tap(self,
                          press_key1, press_key2, tap_key, n=1, interval=0, pre_dl=None, post_dl=None):
        """Press combination of three keys, like Ctrl + Shift + C, The tap key
        could be tapped for multiple time.

        Examples::

            bot.press_and_tap("ctrl", "shift", "c")

        **中文文档**

        按下三个键的组合键。
        """
        press_key1 = self._parse_key(press_key1)
        press_key2 = self._parse_key(press_key2)
        tap_key = self._parse_key(tap_key)

        self.delay(pre_dl)
        self.k.press_key(press_key1)
        self.k.press_key(press_key2)
        self.k.tap_key(tap_key, n, interval)
        self.k.release_key(press_key1)
        self.k.release_key(press_key2)
        self.delay(post_dl)

    def ctrl_c(self, pre_dl=None, post_dl=None):
        """Press Ctrl + C, usually for copy.

        **中文文档**

        按下 Ctrl + C 组合键, 通常用于复制。
        """
        self.delay(pre_dl)
        self.k.press_key(self.k.control_key)
        self.k.tap_key("c")
        self.k.release_key(self.k.control_key)
        self.delay(post_dl)

    def ctrl_v(self, pre_dl=None, post_dl=None):
        """Press Ctrl + V, usually for paste.

        **中文文档**

        按下 Ctrl + V 组合键, 通常用于粘贴。
        """
        self.delay(pre_dl)
        self.k.press_key(self.k.control_key)
        self.k.tap_key("v")
        self.k.release_key(self.k.control_key)
        self.delay(post_dl)

    def ctrl_x(self, pre_dl=None, post_dl=None):
        """Press Ctrl + X, usually for cut.

        **中文文档**

        按下 Ctrl + X 组合键, 通常用于剪切。
        """
        self.delay(pre_dl)
        self.k.press_key(self.k.control_key)
        self.k.tap_key("x")
        self.k.release_key(self.k.control_key)
        self.delay(post_dl)

    def ctrl_z(self, pre_dl=None, post_dl=None):
        """Press Ctrl + Z, usually for undo.

        **中文文档**

        按下 Ctrl + Z 组合键, 通常用于撤销上一次动作。
        """
        self.delay(pre_dl)
        self.k.press_key(self.k.control_key)
        self.k.tap_key("z")
        self.k.release_key(self.k.control_key)
        self.delay(post_dl)

    def ctrl_y(self, pre_dl=None, post_dl=None):
        """Press Ctrl + Y, usually for redo.

        **中文文档**

        按下 Ctrl + Y 组合键, 通常用于重复上一次动作。
        """
        self.delay(pre_dl)
        self.k.press_key(self.k.control_key)
        self.k.tap_key("y")
        self.k.release_key(self.k.control_key)
        self.delay(post_dl)

    def ctrl_a(self, pre_dl=None, post_dl=None):
        """Press Ctrl + A, usually for select all.

        **中文文档**

        按下 Ctrl + A 组合键, 通常用于选择全部。
        """
        self.delay(pre_dl)
        self.k.press_key(self.k.control_key)
        self.k.tap_key("a")
        self.k.release_key(self.k.control_key)
        self.delay(post_dl)

    def ctrl_f(self, pre_dl=None, post_dl=None):
        """Press Ctrl + F, usually for search.

        **中文文档**

        按下 Ctrl + F 组合键, 通常用于搜索。
        """
        self.delay(pre_dl)
        self.k.press_key(self.k.control_key)
        self.k.tap_key("f")
        self.k.release_key(self.k.control_key)
        self.delay(post_dl)

    def ctrl_fn(self, i, pre_dl=None, post_dl=None):
        """Press Ctrl + Fn1 ~ 12 once.

        **中文文档**

        按下 Ctrl + Fn1 ~ 12 组合键。
        """
        self.delay(pre_dl)
        self.k.press_key(self.k.control_key)
        self.k.tap_key(self.k.function_keys[i])
        self.k.release_key(self.k.control_key)
        self.delay(post_dl)

    def alt_fn(self, i, pre_dl=None, post_dl=None):
        """Press Alt + Fn1 ~ 12 once.

        **中文文档**

        按下 Alt + Fn1 ~ 12 组合键。
        """
        self.delay(pre_dl)
        self.k.press_key(self.k.alt_key)
        self.k.tap_key(self.k.function_keys[i])
        self.k.release_key(self.k.alt_key)
        self.delay(post_dl)

    def shift_fn(self, i, pre_dl=None, post_dl=None):
        """Press Shift + Fn1 ~ 12 once.

        **中文文档**

        按下 Shift + Fn1 ~ 12 组合键。
        """
        self.delay(pre_dl)
        self.k.press_key(self.k.shift_key)
        self.k.tap_key(self.k.function_keys[i])
        self.k.release_key(self.k.shift_key)
        self.delay(post_dl)

    def alt_tab(self, n=1, pre_dl=None, post_dl=None):
        """Press Alt + Tab once, usually for switching between windows.
        Tab can be tapped for n times, default once.

        **中文文档**

        按下 Alt + Tab 组合键, 其中Tab键按 n 次, 通常用于切换窗口。
        """
        self.delay(pre_dl)
        self.k.press_key(self.k.alt_key)
        self.k.tap_key(self.k.tab_key, n=n, interval=0.1)
        self.k.release_key(self.k.alt_key)
        self.delay(post_dl)

    #--- Other ---
    def type_string(self, text, interval=0, pre_dl=None, post_dl=None):
        """Enter strings.

        **中文文档**

        从键盘输入字符串, interval是字符间输入时间间隔, 单位是秒。
        """
        self.delay(pre_dl)
        self.k.type_string(text, interval)
        self.delay(post_dl)
        
    def copy_text_to_clipboard(self, text):
        """Copy text to clipboard.

        **中文文档**

        拷贝字符串到剪贴板。
        """
        pyperclip.copy(text)


bot = Bot()
