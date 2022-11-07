from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
from diagrams.aws.network import CloudFront
from diagrams.aws.network import APIGateway
from diagrams.aws.security import ACM
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda
from diagrams.aws.security import IAM
from diagrams.aws.security import IAMRole

with Diagram("Tachyon", show=False):
    wordpress = Custom("Wordpress website", "./img/wordpress.png")
    cert = ACM("ACM SSL certificate")
    api = APIGateway("REST API")

    with Cluster("Image Processing"):
        image_proc = [Lambda("Tachyon Lambda"),
                      S3("S3 Media storage"),
                      CloudFront("CloudFront\nCaching and CDN")]

    with Cluster("IAM"):
        iam = IAM("Tachyon IAM user")
        iam - Edge(color="brown", style="dotted") - IAMRole("Role and policy for\ninteracting with S3")

    wordpress >> Edge(color="firebrick") << image_proc
    cert >> image_proc
    image_proc >> Edge(color="firebrick") << api
    image_proc >> Edge(color="darkgreen") << iam
