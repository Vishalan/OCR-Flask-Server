# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.document_response import DocumentResponse  # noqa: E501
from swagger_server.models.documents_request import DocumentsRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDocumentsController(BaseTestCase):
    """DocumentsController integration test stubs"""

    def test_process_documents(self):
        """Test case for process_documents

        Process list of documents
        """
        body = DocumentsRequest()
        response = self.client.open(
            '/v1/documents',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
