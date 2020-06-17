import json
import pytest

from aws_cdk import core
from cdkdemo.cdkdemo_stack import CdkdemoStack


def get_template():
    app = core.App()
    CdkdemoStack(app, "cdkdemo")
    return json.dumps(app.synth().get_stack("cdkdemo").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
