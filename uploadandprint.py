from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'dataset' not in request.files:
        return redirect(request.url)
    file = request.files['dataset']
    graph_type = request.form.get('graph_type')
    if file.filename == '':
        return redirect(request.url)
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('display_graph', graph_type=graph_type, filename=file.filename))
    return redirect(request.url)

@app.route('/display/<graph_type>/<filename>')
def display_graph(graph_type, filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    df = pd.read_csv(filepath)
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'plot.png')
    plt.figure(figsize=(10, 6))
    
    if graph_type == 'bar':
        avg_price_by_brand = df.groupby('Brand')['Price'].mean().reset_index()
        sns.barplot(x='Brand', y='Price', data=avg_price_by_brand)
        plt.title('Average Smartphone Price by Brand')
    elif graph_type == 'box':
        sns.boxplot(x='Brand', y='Price', data=df)
        plt.title('Distribution of Smartphone Prices by Brand')
    elif graph_type == 'scatter':
        sns.scatterplot(x='Battery', y='Price', hue='Brand', data=df)
        plt.title('Battery Capacity vs. Price')
    elif graph_type == 'donut':
        brand_counts = df['Brand'].value_counts()
        plt.pie(brand_counts, labels=brand_counts.index, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
        plt.title('Proportion of Smartphone Brands')
    
    plt.xticks(rotation=45)
    plt.savefig(img_path)
    plt.close()
    
    return render_template('result.html', graph_url=img_path)

if __name__ == '__main__':
    app.run(debug=True)
