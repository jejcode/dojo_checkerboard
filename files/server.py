from flask import Flask, render_template # import modules

app = Flask(__name__) # create new Flask instance

@app.route('/') # main route to load defaut checkerboard
def default_checkerboard(x = 4, y = 4):
    col = int(y/2) # the loop in checkerboard.html will make 2 boxes for every integer
    return render_template('checkerboard.html', row = x, col = col)

@app.route('/<int:x>') # route for rows determined by user
def custom_rows_checkerboard(x, y = 4):
    col = int(y/2) # the loop in checkerboard.html will make 2 boxes for every integer
    return render_template('checkerboard.html', row = x, col = col)

@app.route('/<int:x>/<int:y>') # route for rows and cols determined by user
def custom_rows_and_cols_checkerboard(x, y):
    col = int(y/2) # the loop in checkerboard.html will make 2 boxes for every integer
    return render_template('checkerboard.html', row = x, col = col)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>') # route for rows, cols, and colors determined by user
def custom_colors_checkerboard(x, y, color1, color2):
    col = int(y/2) # the loop in checkerboard.html will make 2 boxes for every integer
    return render_template('checkerboard.html', row = x, col = col, color1 = color1, color2 = color2)

if __name__ == '__main__':
    app.run(debug = True, port = 8000)