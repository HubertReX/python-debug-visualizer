from Person import Person
import debugvisualizer
import vscodedebugvisualizer as dv
from vscodedebugvisualizer import globalVisualizationFactory
import numpy as np
from json import dumps

# VC Code extension fixes:
# https://github.com/hediet/vscode-debug-visualizer/issues/226
# https://github.com/hediet/vscode-debug-visualizer/pull/215/files

# types of visualizations
# https://hediet.github.io/visualization/?darkTheme=1&theme=dark

# put "x" in the Debug Visualizer and use step by step
# debugging to see the different types of data visualization

# examples of visualizers
# https://gitlab.com/fehrlich/vscode-debug-visualizer-py/-/tree/main/vscodedebugvisualizer/visualizer?ref_type=heads

import json


def serialize(arr):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": {"grid": True},
        "rows": [
            {
                "columns": [
                    {"content": str(value), "tag": str(value)} for value in arr
                ],
            }
        ],
    }
    return json.dumps(formatted)

# dv.visualize(x)


x = 5
x = "asdf"
x = 5.5
x = [1, 2, 3, 4, 5, 6, "a", "b"]
x = ["b", "a", "c", "d", "e"]
x.sort()
x = {
    "asdf1": "123",
    "asdf2": [345, 234],
    #     "asdf3": {"foo": "bar"},
}

x = [1, 2, 3, 4, 5, 6]
# histogram
x = np.concatenate([np.arange(i) for i in range(9)])
x = x.reshape(2, -1)


# one dimension
x = np.arange(100)
x = np.linspace(-np.pi, np.pi, 100)
x = np.sin(x)

# 2 dimension
x = x.reshape(5, 20)
# 2 dimension transpose
x = x.transpose()
x = x.transpose()

# 3 dimensions
x = x.reshape(2, 5, 10)

# 4 dimensions
x = x.reshape(2, 5, 2, 5)

# big number
x = np.empty(2 ** 24)
x[0:1000000] = 1
x[1000000:10000000] = 5

# pyTorch
try:
    import torch

    x = np.concatenate([np.arange(i) for i in range(9)])
    x = x.reshape(2, -1)
    x = torch.Tensor(x)
    pass

except ImportError:
    pass


# tensorflow

try:
    import tensorflow as tf

    x = np.concatenate([np.arange(i) for i in range(9)])
    x = x.reshape(2, -1)
    x = tf.convert_to_tensor(x)
    pass
except ImportError:
    pass


# pandas

try:
    import pandas as pd
    import plotly.express as px

    x = px.data.gapminder().query("year == 2007")
    pass
except ImportError:
    pass

# custom visualizer defined in ./debugvisualizer.py (this file is included automatically)

x = Person("Aria")
globalVisualizationFactory.addVisualizer(debugvisualizer.PersonVisualizer())
parent1 = Person("Eduart")
parent2 = Person("Catelyn")
x.addParent(parent1)
x.addParent(parent2)
parent1.addParent(Person("Benjen"))
# debugvisualizer.PersonVisualizer().visualize(x)

# direct debug-visualizer json as dict with property "kind"

x = {
    "kind": {"dotGraph": True},
    "text": """
    digraph G {
    subgraph cluster_0 {
      style=filled;
      color=lightgrey;
      node [style=filled,color=white];
      a0 -> a1 -> a2 -> a3;
      label = "process #1";
    }

    subgraph cluster_1 {
      node [style=filled];
      b0 -> b1 -> b2 -> b3;
      label = "process #2";
      color=blue
    }
    start -> a0;
    start -> b0;
    a1 -> b3;
    b2 -> a3;
    a3 -> a0;
    a3 -> end;
    b3 -> end;

    start [shape=Mdiamond];
    end [shape=Msquare];
}
""",
}

x = {
    "kind": {"plotly": True},
    "data": [
        {
            "mode": "lines",
            "type": "scatter",
            "x": ["A", "B", "C"],
            "xaxis": "x",
            "y": [4488916, 3918072, 3892124],
            "yaxis": "y",
        },
        {
            "cells": {"values": [["A", "B", "C"], [341319, 281489, 294786], [4488916, 3918072, 3892124]]},
            "domain": {"x": [0.0, 1.0], "y": [0.0, 0.60]},
            "header": {"align": "left", "font": {"size": 10}, "values": ["Date", "Number", "Output"]},
            "type": "table",
        },
    ],
    "layout": {"xaxis": {"anchor": "y", "domain": [0.0, 1.0]}, "yaxis": {"anchor": "x", "domain": [0.75, 1.0]}},
}
pass
