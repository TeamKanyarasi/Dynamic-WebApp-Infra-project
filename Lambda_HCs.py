import boto3

# Initialize clients
ec2 = boto3.client('ec2', region_name='ap-south-1')
elbv2 = boto3.client('elbv2', region_name='ap-south-1')
sns = boto3.client('sns', region_name='ap-south-1')

def lambda_handler(event, context):
    # Get health of the target
    response = elbv2.describe_target_health(
        TargetGroupArn='TARGET_GRP_ARN' # Replace with your Target group Arn
    )
    
    for target in response['TargetHealthDescriptions']:
        # If any target is unhealthy
        if target['TargetHealth']['State'] == 'unhealthy':
            instance_id = target['Target']['Id']
            
            # Create snapshot
            ec2.create_snapshots(
                InstanceSpecification={
                    'InstanceId': instance_id,
                    'ExcludeBootVolume': False,
                    'Description':'This is my snapshot for ' + instance_id
                }
            )
            
            # Terminate the instance
            ec2.terminate_instances(
                InstanceIds=[instance_id]
            )
            
            # Send SNS notification
            sns.publish(
                TopicArn='SNS_TOPIC_ARN', # Replace with your SNS topic Arn
                Message=f'Instance {instance_id} was unhealthy and has been terminated. A snapshot was created for debugging.',
                Subject='Unhealthy EC2 Instance Terminated'
            )
