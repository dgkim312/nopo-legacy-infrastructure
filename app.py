#!/usr/bin/env python3

import aws_cdk as cdk

from nopo_legacy_infrastructure.cdk_vpc_stack import CdkVpcStack
from nopo_legacy_infrastructure.cdk_ec2_stack import CdkEc2Stack
from nopo_legacy_infrastructure.cdk_rds_stack import CdkRdsStack


app = cdk.App()


vpc_stack = CdkVpcStack(app, "nopo-vpc")
ec2_stack = CdkEc2Stack(app, "nopo-ec2",
                        vpc=vpc_stack.vpc)
rds_stack = CdkRdsStack(app, "nopo-rds",
                        vpc=vpc_stack.vpc,
                        asg_security_groups=ec2_stack.asg.connections.security_groups,
                        bastion_security_groups=ec2_stack.bastion.connections.security_groups
                        )


app.synth()
