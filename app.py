from flask import Flask, render_template, request, redirect, send_file, url_for
import os


def check_val():
    with open("image_Name.txt", "r") as file:
        filename = file.readline()

    with open("animal_Name.txt", "r") as file:
        get_answer = file.readline()
        
    return filename , get_answer

 
app = Flask(__name__)
 
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')

@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')

@app.route('/result', methods = ['POST'])
def data():    
    filename , get_answer = check_val() 
    if filename:
 
        if get_answer == "Elephant":
            return render_template('result_Elephant.html', filename=filename)
        elif get_answer == "Dog":
            return render_template('result_Dog.html', filename=filename)
        elif get_answer == "Cat":
            return render_template('result_Cat.html', filename=filename)
        elif get_answer == "Chicken":
            return render_template('result_Chicken.html', filename=filename)
        elif get_answer == "Horse":
            return render_template('result_Horse.html', filename=filename)
        elif get_answer == "Butterfly":
            return render_template('result_Butterfly.html', filename=filename)
        else:
            return render_template('Not_Found.html', filename=filename)
    else:
        return "file Not Found"
    
        
if __name__ == '__main__':
    app.run(host='localhost', port=5500 , debug=True)
    # app.run(host = '192.168.29.29' , port=8080, debug=True)