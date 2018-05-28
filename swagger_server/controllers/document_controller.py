import connexion
import six

from swagger_server.models.document_request import DocumentRequest  # noqa: E501
from swagger_server.models.document_response import DocumentResponse # noqa: E501
from swagger_server import util
from swagger_server.ocr.ocrutils import process_image
from flask import Flask, request, jsonify

def process_document(body):  # noqa: E501
    """Process single document

     # noqa: E501

    :param body: Document URI
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = DocumentRequest.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            url = body.doc_uri
            if 'jpg' in url:
                output = process_image(url)
                return jsonify(DocumentResponse(document_path=url,extracted_text=output,type="jpeg"))
            else:
                return jsonify({"error": "only .jpg files, please"})
        except:
            return jsonify(
                {"error": "Did you mean to send: {'docURI': 'some_jpeg_url'}"}
            )
    return jsonify(
        {"error": "Did you mean to send: {'docURI': 'some_jpeg_url'}"}
    )
