import sys
from importlib import import_module
from pathlib import Path, PurePosixPath
from typing import List


class SysArgumentError(Exception):
    pass


def validate_sys_args(agrs: List[str]):
    if not args:
        raise SysArgumentError('No day selected. Please pass as argument e.g. "python AOC/app.py day-01"')

    # strip arg down to numeric values & add a 0 if single digit
    day = ''.join([x for x in args[0] if x.isnumeric()]).zfill(2)

    if not day:
        raise SysArgumentError('No day number passed in first argument. e.g. "python AOC/app.py day-01"')

    if day not in [str(x).zfill(2) for x in range(1, 26)]:
        raise SysArgumentError('Day number is invalid (must be betwee 1-25). e.g. "python AOC/app.py day-01"')

    return day


def import_day(day_number: str):
    module_name = f"day-{day_number}"
    try:
        return import_module(".app", f"challenges.{module_name}")
    except Exception as ex:
        print(f"Unable to import module: {ex}")
        raise


if __name__ == "__main__":
    _, *args = sys.argv
    day_number = validate_sys_args(args)
    module = import_day(day_number)
    module.main()
