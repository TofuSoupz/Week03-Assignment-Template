# WRITING IN ALL CAPS IS LIKE YELLING

Best to use your "inner voice" sometimes, writing entirely in lowercase.

In a file called `inner.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You're welcome, but not required, to prompt the user explicitly, as by passing a `str` of your own as an argument to `input`.

## Before You Begin
- Open the `inner.py` file.
- In your terminal, change the directory to `02-inner` with
    ```bash
    cd 02-inner
    ```
- Make the necessary changes to `inner.py` as per the instructions.

## How to Run

- Run the script directly in your terminal with `python inner.py`.

## Input

- Prompt the user to write something in all caps, e.g., `HELLO, WORLD!`.

## Expected Output

- If you type `HELLO, WORLD!` and press Enter. Your program should output `hello, world!`.
- If type `THIS IS SPARTA` and press Enter. Your program should output `this is sparta`.
- If you type `2024` and press Enter. Your program should output `2024`.

If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your `02-inner` folder and have saved your `inner.py` file there. Remember how?

## Hints
- Recall that `input` returns a `str`, per [Python's input documentation](https://docs.python.org/3/library/functions.html#input).
- Recall that a `str` comes with the `lower` method, per [docs.python.org/3/library/stdtypes.html#str.lower](https://docs.python.org/3/library/stdtypes.html#str.lower).

## How to Test

- Click on the becker glass icon on the left tab.
- Locate the `02-inner` test. You might need to expand the `week03-assignment` to find it.
- Click on the play arrow to run the test.
- If it is green, the test passed and you should be good to submit this exercise.
- If it is red, you possibly made a mistake. Check the error in the test "Test Results" tab on the view at the bottom of the screen (same location as the Terminal view)

## How to Submit

- Use the VS code Source Control Tab to submit your assignment:
    - Click on the `+` sign next to the files you want to include, in this case `inner.py`
    - Write a commit message, e.g., "Finished with exercise 2."
    - Select "Commit and Push".
- Alternativally, you can use git to add, commit, and push your changes:
    ```bash
    git add inner.py
    git commit -m "Finished with exercise 2."
    git push
    ```
Notice that by doing these steps you are only updating your assignment repository with the solution to this exercise. You still need to work on the other exercises and submit them. 


## Source
- Adapted CS50P