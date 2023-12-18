#!/usr/bin/env python3

from aws_cdk import App

from lambda_s3_trigger.lambda_s3_trigger_stack import S3TriggerStack

app = App()
S3TriggerStack(app, "s3trigger")

app.synth()
