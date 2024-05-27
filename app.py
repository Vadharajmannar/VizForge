from flask import Flask, request, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('visualization.html')

@app.route('/generate_graph', methods=['POST'])
def generate_graph():
    file = request.files['dataset']
    graph_type = request.form['graph_type']
    
    df = pd.read_csv(file)
    
    img = io.BytesIO()

    if graph_type == 'bar':
        df.plot(kind='bar')
    elif graph_type == 'box':
        df.plot(kind='box')
    elif graph_type == 'scatter':
        pd.plotting.scatter_matrix(df)
    elif graph_type == 'donut':
        df.plot(kind='pie', subplots=True)
    
    plt.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
