import boto3

#AWS Credentials and region
aws_access_key_id = 'ACCESS_KEY_ID' # Replace with your access key id
aws_secret_access_key = 'SECRET_ACCESS_KEY' # Replace with your secret access key
region = 'ap-south-1'

def delete_ec2_instance(instance_id):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.terminate_instances(InstanceIds=[instance_id])
    return response

def delete_load_balancer(load_balancer_arn):
    elbv2 = boto3.client('elbv2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region)
    response = elbv2.delete_load_balancer(LoadBalancerArn=load_balancer_arn)
    return response

def delete_auto_scaling_group(auto_scaling_group_name):
    autoscaling = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region)
    response = autoscaling.delete_auto_scaling_group(AutoScalingGroupName=auto_scaling_group_name, ForceDelete=True)
    return response

# Replace these with your actual resource identifiers
instance_id = 'my-instance-id'
load_balancer_arn = 'my-load-balancer-arn'
auto_scaling_group_name = 'my-auto-scaling-group-name'

# Delete EC2 instance
print("Deleting EC2 instance...")
delete_ec2_instance(instance_id)

# Delete ALB
print("Deleting load balancer...")
delete_load_balancer(load_balancer_arn)

# Delete ASG
print("Deleting auto scaling group...")
delete_auto_scaling_group(auto_scaling_group_name)
