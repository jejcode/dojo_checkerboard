# Dojo assignment: checkboard
## Joel Jacobson

Create a new Flask project

Have the root route render a template with a checkerboard on it

Have the css in a separate stylesheet and link this to the template

Have another route accept a single parameter (i.e. "/<x>") and render a checkerboard with x many rows, with alternating colors

NINJA BONUS: Have another route accept 2 parameters (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns, with alternating colors

SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2

## What I learned:
- if, elif, and if/else statements all end with {$ endif %} in jinja2
- in jinja2, numbers are processed as floats unless first converted to integers