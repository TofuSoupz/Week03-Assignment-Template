# Einstein

Even if you haven’t studied physics (recently or ever!), you might have heard that $E=mc^2$, wherein $E$ represents energy (measured in Joules), $m$ represents mass (measured in kilograms), and $c$ represents the speed of light (measured approximately as 300,000,000 meters per second), per [Albert Einstein](https://en.wikipedia.org/wiki/Albert_Einstein) et al. Essentially, the formula means that mass and energy are equivalent.

In the file called `einstein.py`, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

## Before You Begin
- Open the `einstein.py` file.
- In your terminal, change the directory to `03-einstein` with
    ```bash
    cd 03-einstein
    ```
- Make the necessary changes to the code as per the instructions.

## How to Run

- Run the script directly in your terminal with `python einstein.py`.

## Input

Prompt the user for mass as an integer (in kilograms)

## Expected Output

- If you type `1` and press Enter. Your program should output:
  ```
  90000000000000000
  ```
- If type `14` and press Enter. Your program should output:
  ```
  1260000000000000000
  ```
- If you type `50` and press Enter. Your program should output:
  ```
  4500000000000000000
  ```

## Hints
- Recall that `input` returns a `str`, per [Python's documentation on input](https://docs.python.org/3/library/functions.html#input).
- Recall that `int` can convert a `str` to an `int`, per [Python's documentation on int](https://docs.python.org/3/library/functions.html#int).
- Recall that Python comes with several built-in functions, per [Python's built-in functions](https://docs.python.org/3/library/functions.html).


## How to Test

- Click on the becker glass icon on the left tab.
- Locate the `03-einstein` test. You might need to expand the `week03-assignment` to find it.
- Click on the play arrow to run the test.
- If it is green, the test passed and you should be good to submit this exercise.
- If it is red, you possibly made a mistake. Check the error in the test "Test Results" tab on the view at the bottom of the screen (same location as the Terminal view)

## How to Submit

- Use the VS code Source Control Tab to submit your assignment:
    - Click on the `+` sign next to the files you want to include, in this case `einstein.py`
    - Write a commit message, e.g., "Finished with exercise 3."
    - Select "Commit and Push".
- Alternativally, you can use git to add, commit, and push your changes:
    ```bash
    git add einstein.py
    git commit -m "Finished with exercise 3."
    git push
    ```
Notice that by doing these steps you are only updating your assignment repository with the solution to this exercise. You still need to work on the other exercises and submit them. 

## Source
- Adapted from CS50P