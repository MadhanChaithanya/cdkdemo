#!/usr/bin/env python3

from aws_cdk import core

from cdkdemo.cdkdemo_stack import CdkdemoStack


app = core.App()
CdkdemoStack(app, "cdkdemo")

app.synth()
