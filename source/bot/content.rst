Mouse and Keyboard Robot Usage Guide
====================================
First, import::

	>>> from macro.bot import bot

Do some mouse move::

	# Double left click at (600, 600)
	>>> bot.left_click(600, 600, 2)

Single key tap::

	# Tap "a"
	>>> bot.tap_key("a")

	# Tap space 4 times
	>>> bot.tap_key(" ", n=4)

Typing::

	>>> bot.type_string("Hello World!")


Highlight features
------------------
**Pre/Post delay**:

In some case, you need insert a delay before or after your operation. For example, you need a buffer time in between a series of operations. Almost every methods take two option keyword ``pre_dl`` and ``post_dl`` for pre-delay and post-delay.

By default, it's no delay before and after your operation. But if you want to add a default one, you can edit ``bot.dl``. This value is the default pre/post delay time if you don't define it explicitly.

**Key name syntax support**:

You can program Keyboard key by using it's name easily.

::

	>>> bot.tap_key("tab")
	>>> bot.tap_key("del")

For list of key name, check :class:`this <macro.bot.Bot>`.

**Easy Keyboard Combination**:

::

	# Ctrl + C for copy
	>>> bot.press_and_tap("ctrl", "c")

	# Alt + Tab x 2
	>>> bot.press_and_tap("alt", "tab", n=2)