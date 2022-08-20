from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.aws.database import Aurora
from diagrams.aws.network import CloudFront
from diagrams.aws.storage import S3
from diagrams.saas.cdn import Cloudflare
from diagrams.saas.logging import Papertrail
from diagrams.onprem.inmemory import Redis

with Diagram("Website stack"):
    server = Custom("Heroku server", "./img/heroku.png")
    database = Aurora("MySQL database")
    website_cloudfront = CloudFront("CloudFront web caching")
    tachyon_cloudfront = CloudFront("CloudFront media caching")
    s3 = S3("S3 media storage")

    with Cluster("Heroku plugins"):
        plugins = [Redis("Redis cache"),
                   Papertrail("Papertrail logging"),
                   Custom("Process scheduler", "./img/scheduler.png")]

    database \
        >> Edge(color="purple", style="bold") \
    << website_cloudfront \
        >> Edge(color="purple", style="bold") \
    << server \
        >> Edge(color="purple", style="bold") \
        << plugins

    server \
        >> Edge(color="purple", style="bold") \
        << s3 \
            >> Edge(color="purple", style="bold") \
            << tachyon_cloudfront
