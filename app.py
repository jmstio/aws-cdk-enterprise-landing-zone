#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_enterprise_landing_zone.aws_cdk_enterprise_landing_zone_stack import AwsCdkEnterpriseLandingZoneStack


app = core.App()
AwsCdkEnterpriseLandingZoneStack(app, "aws-cdk-enterprise-landing-zone")

app.synth()
