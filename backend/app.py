from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import tempfile
from datetime import datetime
from pubmed_pdf_downloader import PubMedProcessor
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)

PROCESSED_FOLDER = os.path.join(os.getcwd(), "processed_files")
os.makedirs(PROCESSED_FOLDER, exist_ok=True)


@app.route("/upload", methods=["POST"])
def upload_and_process():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    try:
        temp_input_path = os.path.join(tempfile.gettempdir(), 'Pubs.xlsx')
        file.save(temp_input_path)

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        output_filename = f'Pubs_Updated_{timestamp}.xlsx'
        output_path = os.path.join(PROCESSED_FOLDER, output_filename)

        processor = PubMedProcessor(temp_input_path, output_path)
        processor.process()

        if os.path.exists(output_path):
            return send_file(
                output_path,
                as_attachment=True,
                download_name='Pubs_Updated.xlsx',
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
        else:
            return jsonify({'error': 'Processed file not found'}), 500

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
