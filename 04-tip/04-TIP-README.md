
# Tip Calculator

> And now for my Wizard tip calculator.
>
> — Morty Seinfeld

In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. 

Write a Python program that helps you calculate the correct amount to tip at a restaurant. The program should ask you how much your meal cost and what percentage you want to tip. Then, it will calculate the tip amount and tell you how much to leave.

## Before You Begin
- Open the `tip.py` file.
- In your terminal, change the directory to `04-tip` with
    ```bash
    cd 04-tip
    ```
- Make the necessary changes to the code as per the instructions.

## How to Run 

- Run the script directly in your terminal with `python tip.py`

## Inputs

Prompt the user to enter the following information:

- Meal coast
    - Assume that the user will input only numeric values, such: `10` for $10 or `25.43` for $25.43
- Tip amount
    - Assume that the user will input only numeric values, such: `10` for 10% or `12.5` for 12.5%

## Expected Output
- If you type 50.00 for the meal, and type 15 for the tip. Your program should output exactly: `Leave $7.50`
- If you tyoe 100.00 for the meal, and type 18 for the tip. Your program should output exactly: `Leave $18.00`

Make sure the tip amount is displayed with exactly two numbers after the decimal point.

## Hints
- Recall that `input` returns a `str`, per [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recall that `float` can convert a `str` to a `float`, per [docs.python.org/3/library/functions.html#float](https://docs.python.org/3/library/functions.html#float).


## Challenge (optional)

- Accept meal inputs with `$`, e.g., `$10`
- Accept tip inputs with `%`, e.g., `15%` 

Recall that a `str` comes with the `replace` method, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## How to Test

- Click on the becker glass icon on the left tab.
- Locate the `04-tip` test. You might need to expand the `week03-assignment` to find it.
- Click on the play arrow to run the test.
- If it is green, the test passed and you should be good to submit this exercise.
- If it is red, you possibly made a mistake. Check the error in the test "Test Results" tab on the view at the bottom of the screen (same location as the Terminal view)

## How to Submit

- Use the VS code Source Control Tab to submit your assignment:
    - Click on the `+` sign next to the files you want to include, in this case `tip.py`
    - Write a commit message, e.g., "Finished with assignment 03"
    - Select "Commit and Push".
- Alternativally, you can use git to add, commit, and push your changes:
    ```bash
    git add tip.py
    git commit -m "Finished with assignment 3"
    git push
    ```
 
## Source
- Adapted from CS50P