from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.aws.database import Aurora
from diagrams.saas.cdn import Cloudflare
from diagrams.saas.logging import Papertrail
from diagrams.onprem.inmemory import Redis

with Diagram("Website stack"):
    server = Custom("Heroku server", "./img/heroku.png")
    database = Aurora("MySQL database")

    with Cluster("Heroku plugins":
