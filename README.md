# Visual Debugging in VS Code

## How to use visual debugger in VS Code with Python

Install VS Code extension:

[Market Place](https://marketplace.visualstudio.com/items?itemName=hediet.debug-visualizer)

Install Python module:

`pip install vscodedebugvisualizer`

In your script import this module:

> import vscodedebugvisualizer as dv
> from json import dumps
>
> x = ["b", "a", "c", "d", "e"]
> x.sort()

Add breakpoint at line with sorting and run the script using VS Code debugger.

Open new visualizer window (use the command `Debug Visualizer: New View`)

enter `dv.visualize(x)` in expression field.
