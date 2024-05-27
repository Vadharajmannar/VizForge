from flask import Flask, request, render_template, redirect, url_for
import os
import pandas as pd
import matplotlib.pyplot as plt
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('templates/another.html')  # Entry page to select and upload dataset

@app.route('/', methods=['POST'])
def generate_graph():
    # Check if file is uploaded
    if 'dataset' not in request.files:
        return "No file uploaded"

    dataset = request.files['dataset']

    # Check if file is not empty
    if dataset.filename == '':
        return "Empty file uploaded"

    # Check if file is a CSV
    if not dataset.filename.endswith('.csv'):
        return "Only CSV files are supported"

    # Generate a unique filename for the output graph
    filename = f"static/visualizations/{uuid.uuid4()}.png"

    # Create a directory to save visualizations if it doesn't exist
    if not os.path.exists("static/visualizations"):
        os.makedirs("static/visualizations")

    # Load dataset from uploaded file
    try:
        df = pd.read_csv(dataset)
    except Exception as e:
        return f"Error reading CSV file: {str(e)}"

    # Determine which graph to generate
    graph_type = request.form.get('graph_type')
    
    # Generate the graph based on selected type
    try:
        if graph_type == 'bar':
            df.plot(kind='bar')
        elif graph_type == 'box':
            df.plot(kind='box')
        elif graph_type == 'scatter':
            df.plot(kind='scatter', x=df.columns[0], y=df.columns[1])
        elif graph_type == 'donut':
            plt.pie(df.iloc[:, 1], labels=df.iloc[:, 0], wedgeprops=dict(width=0.3))
        else:
            return "Invalid graph type selected"
        
        plt.title(f'{graph_type.capitalize()} Graph')
        plt.tight_layout()  # Adjust layout to prevent clipping
        plt.savefig(filename)
        plt.close()  # Close the plot to free up memory
    except Exception as e:
        return f"Error generating the graph: {str(e)}"

    # Redirect to the visualization info page with generated graph
    return redirect(url_for('templates/visualization_info.html', img=filename, title=f'{graph_type.capitalize()} Graph', info=f'This is a {graph_type} graph'))

@app.route('/visualization_info')
def visualization_info():
    img = request.args.get('img')
    title = request.args.get('title')
    info = request.args.get('info')
    return render_template('templates/visualization_info.html', image_path=img, graph_title=title, graph_info=info)

if __name__ == '__main__':
    app.run(debug=True)
