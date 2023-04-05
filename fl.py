from flask import Flask, render_template
import boto3

app = Flask(__name__)

# AWS Credentials
AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'
AWS_REGION = 'your-region'

# AWS Services
ec2 = boto3.client('ec2', region_name=AWS_REGION,
                   aws_access_key_id=AWS_ACCESS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
lambda_ = boto3.client('lambda', region_name=AWS_REGION,
                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
s3 = boto3.client('s3', region_name=AWS_REGION,
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
dynamodb = boto3.client('dynamodb', region_name=AWS_REGION,
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
cloudwatch = boto3.client('cloudwatch', region_name=AWS_REGION,
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
cloudfront = boto3.client('cloudfront', region_name=AWS_REGION,
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
route53 = boto3.client('route53', region_name=AWS_REGION,
                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
acm = boto3.client('acm', region_name=AWS_REGION,
                   aws_access_key_id=AWS_ACCESS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Portal homepage
@app.route('/')
def index():
    return render_template('index.html')

# Portal endpoints
@app.route('/ec2')
def ec2_page():
    instances = ec2.describe_instances()
    return render_template('ec2.html', instances=instances)

@app.route('/lambda')
def lambda_page():
    functions = lambda_.list_functions()
    return render_template('lambda.html', functions=functions)

@app.route('/s3')
def s3_page():
    buckets = s3.list_buckets()
    return render_template('s3.html', buckets=buckets)

@app.route('/dynamodb')
def dynamodb_page():
    tables = dynamodb.list_tables()
    return render_template('dynamodb.html', tables=tables)

@app.route('/cloudwatch')
def cloudwatch_page():
    alarms = cloudwatch.describe_alarms()
    return render_template('cloudwatch.html', alarms=alarms)

@app.route('/cloudfront')
def cloudfront_page():
    distributions = cloudfront.list_distributions()
    return render_template('cloudfront.html', distributions=distributions)

@app.route('/route53')
def route53_page():
    zones = route53.list_hosted_zones()
    return render_template('route53.html', zones=zones)

@app.route('/acm')
def acm_page():
    certificates = acm.list_certificates()
    return render_template('acm.html', certificates=certificates)

if __name__ == '__main__':
    app.run()
