def display(lives):
    """
    This function returns a multi-lined
    representation state of the hang-man
    based on the lives (index) left.
    """
    hangMan = ["""
/------------
|           |
|           0
|          /|\\
|           |
|          / \\
-------------""",
"""
/------------
|           |
|           0
|          /|\\
|           |
|
-------------""",
"""
/------------
|           |
|           0
|          /|\\
|
|
-------------""",
"""
/------------
|           |
|           0
|
|
|
-------------""",
"""
/------------
|           |
|
|
|
|
-------------"""]
    return (hangMan[lives])