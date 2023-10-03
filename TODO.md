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

Current:

For the near future:

- Move project on python 3.12
- Fix all linters messages
    - Simplify comparations in processing_num_luk()
    - Fix R1710: 'inconsistent-return-statements' pylint message
    - Avoid global variables
    - Fix R1714: 'consider-using-in' pylint message
    - Split long lines into shorters. Fix C0301: 'line-too-long' pylint message
- Document whole project: docstrings, comments, review, README
    - Document modules, classes, functions, methods
        - Fix C0114: 'missing-module-docstring' pylint message
        - Fix : 'missing-class-docstring' pylint message
        - Fix C0116: 'missing-function-docstring' pylint message
        - Fix C0112: 'empty-docstring' pylint message
        - config:4: Использовать многоязычный docstrings (PEP 257? Sphinx? docutils?), не в функции, а отдельным файлом
    - Document algorithm of creating password
    - Update ReadMe
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
- Name all entities correctly
    - Fix one letter names (C0103: 'invalid-name' pylint message)
        - gen_pass:42: переименовать переменную s
- Make linters check only new code
- Launch linters during commit and during push using git hooks and pre-commit framework
- Isolate work with password in one module

For the long future:

- Move Qt GUI from Qt 5 to Qt 6
- Learn how to work with Qt framework
- Refactor Qt GUI
    - Don't use bare 'except'. Fix W0702 'bare-except' pylint message
    - Divide god class UIGP
        qt_gui.py: too-many-instance-attributes, too-many-locals, too-many-statements, attribute-defined-outside-init
    - Avoid duplicate code
        - Components (QLabel + QLineEdit + QCheckBox) for Private Key and for Landmark Phrase are the same
        - There are two methods with 'get_luk_symbols_number()' name
        - Code for password generation
    - Rename UIGP class
    - Initialize all attributes inside \_\_init\_\_
    - Fix E1136: 'unsubscriptable-object' pylint message in Qt GUI.
        It's false positive, so I've just suppressed it.
        But it need to be fixed because of update to new Qt 6.
- Port project on Android
- Pack project into apk
- Pack project into executable file (Win, Linux)
- Learn how to work with beeware framework
- Develop GUI on beeware
- Learn how to work with Kivy framework
- Develop GUI on Kivy
- Develop TUI
