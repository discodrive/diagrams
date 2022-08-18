from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.aws.database import Aurora
from diagrams.aws.network import CloudFront
from diagrams.aws.security import ACM
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda

with Diagram("Tachyon", show=False):
    wordpress = Custom("Wordpress website", "./img/wordpress.png")
    cert = ACM("SSL certificate")

    with Cluster("Image Processing"):
        image_proc = [Lambda("Tachyon Lambda"),
                      S3("Media storage"),
                      CloudFront("Caching and CDN")]

    
    wordpress >> image_proc
    cert >> image_proc
