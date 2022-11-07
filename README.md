# Diagrams of Heroku/AWS architectures

## Diagrams included

### Typical website stack

Our website stacks usually comprise of a Heroku server hosting a WordPress website, which interacts with AWS services. These include S3 buckets for asset storage, RDS for databases and CloudFront for caching/CDN.

#### Services in the stack

- Relational Database Service: The databases used on both staging and live websites are AWS Aurora databases
- S3: Typically 3 buckets for assets, logs and lambda functions
- CloudFront: Live and Staging site distributions and a separate distribution for Tachyon image processing/serving (See below).
- Certifiacte Manager: A wildcard certificate used for the CloudFront distributions.

### Tachyon image processing

Image processing on the site, and an image specific CDN are set up using [Humanmades Tachyon plugin](https://github.com/humanmade/tachyon).

Services provisioned for Tachyon include:

- 3 S3 buckets for:
	- Assets (can use existing bucket if one exists)
	- Tachyon lambda function
	- Tachyon logs
- Amazon certificate - either existing Wildcard certificate or a certificate for `images.domainname.com`
- REST API gateway
- CloudFront distribution to communicate with the S3 assets bucket
- A custom cache policy for non-image media to ensure Tachyon doesn't try to process PDFs/docs/video files
- IAM user to interact with the Lambda function (includes a custom policy role to allow logging to the S3 logs bucket, as well as getting objects from the assets bucket)
- Lambda function to do the actual image processing - comes from a zip file in the S3 bucket
