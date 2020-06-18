from aws_cdk import (
    aws_ec2 as ec2,
    core
)

class CdkdemoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        prj_name = self.node.try_get_context("project_name")
        env_name = self.node.try_get_context("env")

        vpc =ec2.Vpc(self, 'devVPC')