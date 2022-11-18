import aws_cdk as core
import aws_cdk.assertions as assertions

from nopo_legacy_infrastructure.nopo_legacy_infrastructure_stack import NopoLegacyInfrastructureStack

# example tests. To run these tests, uncomment this file along with the example
# resource in nopo_legacy_infrastructure/nopo_legacy_infrastructure_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = NopoLegacyInfrastructureStack(app, "nopo-legacy-infrastructure")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
