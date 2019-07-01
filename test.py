import boto3
import click

session = boto3.Session(profile_name='awsservices')
ec2 = session.resource('ec2')

@click.command()
def list_instance():
    "List EC2 Instances"
    for i in ec2.instances.all(): 
        print(i.id, i.instance_type, i.public_ip_address, i.state['Name'])
    return

if __name__ == '__main__':
    list_instance()
    