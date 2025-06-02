from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        nama = request.form['nama']
        pesan = request.form['pesan']
        
        with open('data.txt', 'a') as file:
            file.write(f"{nama}: {pesan}\n")

            return redirect('/')
    

    with open('data.txt', 'r') as file:
        lines = file.readlines()
    
    return render_template('home.html', lines=lines)

if __name__ == "__main__":
    app.run(debug=True)