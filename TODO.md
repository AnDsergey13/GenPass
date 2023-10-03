Done:

- Separate work with operating system
- Create config system
- Use linters in project
- Create localization system
- Transit Qt GUI on new localization system
- Repair and launch Qt GUI
- Remove unnecessary decorators
- Learn how to correct rename file in Git
- Fix all linters messages
    - Correct typo 'zucing' in gen_pass
- Make linters detect virtual environment
- Move Qt GUI from Qt 5 to Qt 6
- Move project on python 3.12 - not possible because of Qt
    - [x] Upgrade python
    - [x] Make python 3.12 default
    - [x] Move pipx
    - [x] Move venv / PyQt - fail
    - [x] Move linters

Current:

For the near future:

- Fix all linters messages
    - Simplify comparations in processing_num_luk()
    - Fix R1714: 'consider-using-in' pylint message
    - Split long lines into shorters. Fix C0301: Line too long (line-too-long) pylint message
    - Fix R1705: Unnecessary "else / elif" after "return" (no-else-return) pylint message
    - Fix R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements) pylint message
    - Do not use global variables
        - Fix W0603: Using the global statement (global-statement) pylint message
        - Fix C0103: Constant name doesn't conform to UPPER_CASE naming style (invalid-name) pylint message
- Document whole project: docstrings, comments, review, README
    - Document modules, classes, functions, methods
        - Fix C0114: 'missing-module-docstring' pylint message
        - Fix : 'missing-class-docstring' pylint message
        - Fix C0116: 'missing-function-docstring' pylint message
        - Fix C0112: 'empty-docstring' pylint message
        - config:4: Использовать многоязычный docstrings (PEP 257? Sphinx? docutils?), не в функции, а отдельным файлом
    - Document algorithm of creating password
    - Update ReadMe
- Use ruff
    - [x] Get ruff
    - [x] Enable ruff
    - [ ] Learn ruff
    - [ ] Tune ruff
- Tune scopes of all entities (private, public)
- Fix all TODO and FIXME comments (W0511: 'fixme') pylint message
    - Update localization. config: Предусмотреть локализацию
    - config:42: Сделать проверку корректности введённого имени
    - config:109: Сделать проверку try/except для типа вводимого сообщения
    - gen_pass: Вынести в отдельный метод config.get_full_luk_path()
    - localization:10: Переместить в config?
    - localization:16: Кажется здесь неправда, так как возвращаются данные, а не файл
    - localization:37: Выделить из методов add_key_in_all_lang и del_key_in_all_lang повторяющийся код
    - main:24: Переместить код в функцию \_\_main\_\_()
    - system.py:9-45: Переделать
    - system.py:50: Упростить логику, используя значение по умолчанию
    - system.py:55: os.separator?
    - system.py:57: Разница между os.path.isfile и os.path.exists?
    - system.py:92: Переписать?
- Name all entities correctly
    - Fix one letter names (C0103: 'invalid-name' pylint message)
        - gen_pass:42: переименовать переменную s
- Make linters check only new code
- Launch linters during commit and during push using git hooks and pre-commit framework
- Isolate work with password in one module
- Переработка модуля gen_pass
	- Проверить количественное распределение автокоррекционных чисел(step = 8). То есть, при автокореекции числа, какие символы чаще всего используются.
		- Написать гениратор
	- В случае сильного смещения, проверить, как это влияет на безопасность??

For the long future:

- Learn how to work with Qt framework
- Refactor Qt GUI
    - Don't use bare 'except'. Fix W0702: No exception type(s) specified (bare-except) pylint message
    - Divide god class UIGP
        Fix too-many-instance-attributes, too-many-locals, too-many-statements, attribute-defined-outside-init pylint messages
    - Avoid duplicate code. Fix 'duplicate-code' pylint message
        - Components (QLabel + QLineEdit + QCheckBox) for Private Key and for Landmark Phrase are the same
        - There are two methods with 'get_luk_symbols_number()' name
        - Code for password generation
    - qt_gui.py:91: Maybe use with expression and tuple for typical actions?
    - Rename UIGP class
    - Initialize all attributes inside \_\_init\_\_
    - Fix E1136: 'unsubscriptable-object' pylint message in Qt GUI.
        It's false positive, so I've just suppressed it.
        But it need to be fixed because of update to new Qt 6.
    - qt_gui.py:70: Заменить на QApplication.windowIcon
- Port project on Android
- Pack project into apk
- Pack project into executable file (Win, Linux)
- Learn how to work with beeware framework
- Develop GUI on beeware
- Learn how to work with Kivy framework
- Develop GUI on Kivy
- Develop TUI
- Переработка LUK файла
	- Использовать зашифованный контейнер, вместо открытого файла?
		- Где будет храниться ключ от контейнера?
			- Ввод пароля от пользователя? Не слишком ли сложно?
	- Передача(генерация?) между устройствами, с помощью QR кода
