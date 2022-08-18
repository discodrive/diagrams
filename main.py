from diagrams import Diagram
from diagrams.aws.database import Aurora
from diagrams.aws.network import CloudFront
from diagrams.aws.security import ACM
from diagrams.aws.storage import S3
from diagrams.aws.compute import Lambda

with Diagram("Web Service", show=False):
    Aurora("database") >> S3("media storage") >> CloudFront("caching and CDN")
