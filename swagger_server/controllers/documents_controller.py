import connexion
import six

from swagger_server.models.document_response import DocumentResponse  # noqa: E501
from swagger_server.models.documents_request import DocumentsRequest  # noqa: E501
from swagger_server import util
from swagger_server.ocr.ocrutils import process_image
from flask import Flask, request, jsonify

def process_documents(body):  # noqa: E501
    """Process list of documents

     # noqa: E501

    :param body: Array of document URIs
    :type body: dict | bytes

    :rtype: List[DocumentResponse]
    """
    if connexion.request.is_json:
        body = DocumentsRequest.from_dict(connexion.request.get_json())  # noqa: E501
        documentResponseList = []
        try:
            urls = body.doc_ur_is
            for url in urls:
                if 'jpg' in url:
                    output = process_image(url)
                    documentResponseList.append(DocumentResponse(document_path=url,extracted_text=output,type="jpeg"))
        except:
            return jsonify(
                {"error": "Did you mean to send: {'docURIs': 'array of URIs'}"}
            )
    return jsonify(documentResponseList)
