Done:

- Separate work with system
- Create config system
- Use linters in project
- Create localization system
- Transit Qt GUI on new localization system
- Repair and launch Qt GUI
- Remove unnecessary decorators
- Learn how to correct rename file in Git
- Fix all linters messages
    - Correct typo 'zucing' in gen_pass

Current:

- Fix all linters messages
    - Fix [unsubscriptable-object / E1136][1] pylint message in Qt GUI
    - Simplify comparations in processing_num_luk()
    - Fix R1710: 'inconsistent-return-statements' pylint message
    - Avoid global variables
    - Fix R1714: 'consider-using-in' pylint message
    - Make linters detect virtual environment
    - Split long lines into shorters
- Document whole project: docstrings, comments, review, README
    - Document algorithm of creating password
    - Update ReadMe
- Tune scopes of all entities (private, public) [WIP]
- Fix all TODO and FIXME comments
- Correct name of all entities [WIP]
    - Fix one letter names

For the near future:

- Make linters check only new code
- Launch linters during commit and during push using git hooks and pre-commit framework
- Isolate work with password in one module [WIP]

For the long future:

- Learn how to work with Qt framework [WIP]
- Refactor Qt GUI [WIP]
    - Don't use bare 'except'
    - Divide god class UIGP
    - Rename UIGP class
    - Avoid duplicate code
        - Components (QLabel + QLineEdit + QCheckBox) for Private Key and for Landmark Phrase are the same
        - There are two methods with 'get_luk_symbols_number()' name
        - Code for password generation
    - Initialize all attributes inside \_\_init\_\_
- Port project on Android
- Pack project into apk
- Pack project into executable file
- Learn how to work with Kivy framework
- Develop GUI on Kivy
- Develop TUI

[1]: <https://pylint.pycqa.org/en/latest/user_guide/messages/error/unsubscriptable-object.html> (unsubscriptable-object / E1136)
