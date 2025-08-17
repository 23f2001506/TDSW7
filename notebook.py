# 23f2001506@ds.study.iitm.ac.in

import marimo as mo

# ---
# Cell 1: Load data
# This cell initializes two variables: x and y
# Any downstream cell using x or y will automatically re-run if these change
x = list(range(1, 11))
y = [val**2 for val in x]

# ---
# Cell 2: Interactive slider
# The slider controls the index into our dataset
slider = mo.ui.slider(1, len(x), value=5)

# ---
# Cell 3: Select values based on slider
# This cell depends on both the slider and x, y from Cell 1
idx = slider.value - 1
selected_x = x[idx]
selected_y = y[idx]

# ---
# Cell 4: Dynamic Markdown
# Displays the chosen values interactively
mo.md(f"""
### 📊 Interactive Data Point
Selected index: **{slider.value}**

- x = {selected_x}
- y = {selected_y}

{"🟢" * slider.value}
""")
