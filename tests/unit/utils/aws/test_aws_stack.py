import os
import unittest
from unittest import mock

from localstack import config
from localstack.utils.aws.aws_stack import get_local_service_url


class AwsStackTest(unittest.TestCase):
	@mock.patch.dict(os.environ, {'TEST_S3_URL': 'test_s3_url'})
	@mock.patch.dict(os.environ, {'TEST_SAGEMAKER_RUNTIME_URL': 'test_sagemaker_url'})
	@mock.patch.dict(os.environ, {'TEST_DYNAMODB_URL': 'test_dynamodb_url'})
	def test_get_local_service_url(self):
		config.LOCALSTACK_HOSTNAME = 'test_hostname'
		self.assertEqual(get_local_service_url(10101), 'http://test_hostname:10101')
		self.assertEqual(get_local_service_url('s3api'), 'test_s3_url')
		self.assertEqual(get_local_service_url('runtime.sagemaker'), 'test_sagemaker_url')
		self.assertEqual(get_local_service_url('dynamodb'), 'test_dynamodb_url')
