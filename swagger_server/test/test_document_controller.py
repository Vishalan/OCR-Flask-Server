# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.document_request import DocumentRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDocumentController(BaseTestCase):
    """DocumentController integration test stubs"""

    def test_process_document(self):
        """Test case for process_document

        Process single document
        """
        body = DocumentRequest()
        response = self.client.open(
            '/v1/documents/document',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
