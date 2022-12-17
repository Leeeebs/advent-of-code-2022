# Advent of code 2022

> [Advent of Code](https://adventofcode.com/2022/) is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language.

Each day of December poses a new 2-part challenge of varing difficulty.

This repo contains my solutions, written in Python.


Theres a Makefile to make life easier:
`make env` to build the venv
`make run day=<day-number>` to run the app.

e.g.
```python
make env
make run day=2
```

If you don't wanna use Makefiles:
Using Poetry:
- `poetry install`

Manual:
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

To Run:
- `source .venv/bin/activate`
- `python AOC/app.py <day-number>`

e.g.
```python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python AOC/app.py 2
```
