import json
from typing import Generator


class Device:
    """A class to represent a conputer device with a file system"""
    class File:
        """A class to represent a file on a Device"""
        def __init__(self, name: str, size: int) -> None:
            self.name = name
            self.size = size

        def __add__(self, other) -> int:
            """allow files to be added together"""
            return self.size + other.size

    class Directory:
        """A class to represent a directory in a Device's file tree"""
        def __init__(self, name: str) -> None:
            self.name = name
            self._files = {}
            self._child_dirs = {}

        def __iter__(self) -> Generator:
            """allow directories to be used in sum() to get _files total"""
            for file in self._files.values():
                yield file.size

        @property
        def size(self) -> int:
            return sum(self) + sum([x.size for x in self._child_dirs.values()])

        def json(self) -> str:
            """Make obj json serializable"""
            return json.dumps(self, default=lambda x: x.__dict__)

        def size_breakdown(self) -> dict:
            """Recursive size breakdown for current dir & all child dirs"""
            return {
                **{"size": self.size},
                **{
                    k: v.size_breakdown()
                    for k, v in self._child_dirs.items()
                },
            }

    _file_tree = {}
    _fifo_pointer = []
    _dir_ref = None

    @classmethod
    def cd(cls, value: str) -> None:
        """
        Change directory.

        Explanation:
            - Directory objs are stored in a nested dict structure to mimic a file tree.
            - `_fifo_pointer` is a list of dict keys to represent a path to the current dir.
                - `cd <dir>` appends a key to the list (and adds a nested dict level)
                - `cd ..` removes the last key from the list (thus moving up a nested dict level)
            - `_fifo_pointer` is used to find & store a reference obj to the current nested dict in `_dir_ref`.
                - this allows us to update the `_dir_ref` obj & affect the `_file_tree` at the same time.

        Flow:
            - cd() is called with a dir name (key).
            - first, update the _fifo_pointer.
            - loop over each key in the _fifo_pointer list & set the nested file_tree obj in _dir_ref.
            - when the loop is finished _dir_ref is a reference to the current nested obj in _file_tree.
            - any updates to the stored obj will update the _file_tree.

            Adding child directories:
                - use `add_dir()` function on _dir_ref to add a new Directory to the child_dirs dict.

            Adding files:
                - use `add_file()` function on _dir_ref to add a new File to the files dict.
        """
        # update fifo pointer
        if value == "..":
            cls._fifo_pointer.pop()
        else:
            cls._fifo_pointer.append(value)

        # set _file_tree ref obj using pointer list
        cls._dir_ref = cls._file_tree
        for dir_name in cls._fifo_pointer:
            try:
                # get existing Directory obj
                if isinstance(cls._dir_ref, dict):
                    # root level is stored in a dict
                    cls._dir_ref = cls._dir_ref[dir_name]
                elif isinstance(cls._dir_ref, cls.Directory):
                    # all sub directories are in the parent Direcory's _child_dirs
                    cls._dir_ref = cls._dir_ref._child_dirs[dir_name]

            except KeyError:
                # Directory doesn't exist, add new one
                # (based on puzzle_input.txt, this only happens for root dir)
                cls._dir_ref[dir_name] = cls.Directory(value)
                cls._dir_ref = cls._dir_ref[dir_name]

    @classmethod
    def add_dir(cls, name: str) -> None:
        """Add a child Directory to the current Directory"""
        cls._dir_ref._child_dirs[name] = cls.Directory(name)

    @classmethod
    def add_file(cls, size: str, name: str) -> None:
        """Add a File obj to the current Directory"""
        cls._dir_ref._files[name] = cls.File(name, int(size))

    @classmethod
    def file_tree(cls) -> dict:
        """Get JSON serialised file tree"""
        return {
            k: json.loads(v.json())
            for k, v in cls._file_tree.items()
        }

    @classmethod
    def file_sizes(cls) -> dict:
        """Get a size breakdown of every directory in the file tree"""
        return {
            k: v.size_breakdown()
            for k, v in cls._file_tree.items()
        }

    @classmethod
    def total_size(cls) -> int:
        root_dir = list(cls._file_tree.keys())[0]
        return cls.file_sizes()[root_dir]["size"]
