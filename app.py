from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/nilai')
def nilai():
    file_path = os.path.join(os.path.dirname(__file__), 'data_nilai.csv')
    df = pd.read_csv(file_path)

    data_html = df.to_html(classes='table table-striped', index=False)

    stats = {
        'mean': df['nilai'].mean(),
        'max': df['nilai'].max(),
        'min': df['nilai'].min(),
        'max_students': df[df['nilai'] == df['nilai'].max()].to_dict(orient='records'),
        'min_students': df[df['nilai'] == df['nilai'].min()].to_dict(orient='records'),
    }

    return render_template('nilai.html', data_html=data_html, stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
