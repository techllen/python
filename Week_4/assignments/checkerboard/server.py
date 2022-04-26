from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def checkerboard_8_by_8():
    return render_template('checkerboard.html',rows = 8,columns = 8)

@app.route('/<int:rows>')
def checkerboard_rows_by_8(rows):
    return render_template('checkerboard.html',rows = rows ,columns = 8)

@app.route('/<int:rows>/<int:columns>')
def checkerboard_rows_by_columns(rows,columns):
    return render_template('checkerboard.html',rows = rows,columns = columns)

@app.route('/<int:rows>/<int:columns>/<string:color1>/<string:color2>')
def checkerboard_color(rows,columns,color1,color2):
    return render_template('checkerboard.html',rows = rows,columns = columns,color1 = color1,color2 = color2)

if __name__=="__main__":
    app.run(debug=True)  