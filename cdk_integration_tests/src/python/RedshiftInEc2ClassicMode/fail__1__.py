from aws_cdk import core
from aws_cdk import aws_redshift as redshift

class MyRedshiftClusterStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define Redshift Cluster with a specific Cluster Subnet Group name
        redshift.CfnCluster(
            self, 'MyRedshiftCluster',
        )

app = core.App()
MyRedshiftClusterStack(app, "MyRedshiftClusterStack")
app.synth()
