# Lesson Plan

## Workshop Overview _(all together)_

> ~10 minutes

The workshop instructor will introduce the main concepts of this workshop:

- Introduce the workshop's
  [learning objectives](./README.md#learning-objectives).
- Discuss the difference between a function's
  [behavior, strategy and implementation](./behavior_strategy_implementation.md).

## Behavior, Strategy, Implementation _(small groups)_

> ~15 minutes

Explore and discuss the examples in
[behavior, strategy and implementation](./behavior-strategy-implementation.md).

## Introduce the Exercises _(all together)_

> ~15 minutes

- Each group will have 1 minute to share:
  - One thing they couldn't understand
  - One interesting thing they learned
- Discuss why documenting and testing important.
- The instructor does a guided walk through the `/examples` folder, reading and
  running each file:
  - `<module_name>.py`, `test_<module_name>.py`, `<module_name>_sandbox.py`
  - How to study and run each file
  - Demonstrate how to use the
    [Code Review Checklist](./code-review-checklists.md)
  - Demonstrate use the console to read docstrings and run doctests
- Introduce the group exercise

## Document and Test the Mystery Functions _(small groups)_

> ~30 minutes

You will work on the `/exercises` in small groups. You are not expected to
finish all of the exercises during the workshop, you may not even finish all of
the steps for one mystery function. That's ok! There are extra exercises so you
can keept practicing after the workshop.

Study one mystery function at a time following these steps:

1. Explore the mystery function using `<module_name>_sandbox.py`. :
   - There are no wrong answers! Try passing all sorts of arguments until you
     think you understand the function's _behavior_.
2. Describe the function's behavior in `<module_name>.py`:
   - Give the function a descriptive name and rename the files to match.
   - Write type annotations for the function
   - Write a first draft docstring, you can always update it later
3. Write black box unit tests for the function in `test_<module_name>.py`:
   - Ask yourself: _How can I break my program?_
   - Write as many boundary cases as you can
4. Study the function's code to understand its strategy:
   1. Change the variable names to something helpful
   1. Write comments when necessary to explain the function's strategy
5. Take your code to the next level:
   1. Write clear and helpful assertions in the function
   1. Write unit tests for your assertions
   1. Write glass box tests for the function's implementation

## Discussion _(all together)_

> ~20 minutes

Back together, you will have an informal discussion with the other groups and
the workshop leader.

1. Each group will have 2-3 minutes to share:
   - One thing they couldn't figure out
   - One surprising thing they learned
   - One thing they'd like to discuss with the full class
2. Discuss!
