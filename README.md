# Typing stubs for neomodel

## Usage

Install this package with:
```
pip install git+https://github.com/laurentS/neomodel-stubs
```

`mypy` (or any typing tool you're using) should now be able to pick up the annotations.

Note that this probably won't work with python < 3.5

## Notes

These are only very partial stubs still:

- `mypy` should recognize properties for their correct type:
  ```python
  class MyNode(StructuredNode):
      myprop = StringProperty()

  my_node = MyNode()
  # my_node.myprop is seen as str
  ```
- `MyNode.nodes.get()` and other methods will return the wrong type, leading to errors on subsequent lines.
- There are most likely other problems that need fixing. Please open an issue if you spot something broken. PRs welcome :)
