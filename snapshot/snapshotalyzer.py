import boto3
import click 


# Make sure to have access to ec2 each time it is run
session = boto3.Session(profile_name='snapshotalyzer')
ec2 = session.resource('ec2')

# Make listing instances as a function

@click.command()
def list_instances():
	"List Ec2 instances" # using click --help will give this
	for i in ec2.instances.all():
                print(', '.join((
			i.id,
			i.instance_type,
			i.placement['AvailabilityZone'],
			i.state['Name'],
			i.public_dns_name)))

	return

if __name__ == '__main__':
	list_instances()



