import sys
import csv

def getCidr(ip, subnet):
	"""
	Args:
		String of IP from one IP/Subnet combo
		String of subnet from one IP/Subnet combo
	"""
	masks = [
		'0.0.0.0',
		'128.0.0.0',
		'192.0.0.0',
		'224.0.0.0',
		'240.0.0.0',
		'248.0.0.0',
		'252.0.0.0',
		'254.0.0.0',
		'255.0.0.0',
		'255.128.0.0',
		'255.192.0.0',
		'255.224.0.0',
		'255.240.0.0',
		'255.248.0.0',
		'255.252.0.0',
		'255.254.0.0',
		'255.255.0.0',
		'255.255.128.0',
		'255.255.192.0',
		'255.255.224.0',
		'255.255.240.0',
		'255.255.248.0',
		'255.255.252.0',
		'255.255.254.0',
		'255.255.255.0',
		'255.255.255.128',
		'255.255.255.192',
		'255.255.255.224',
		'255.255.255.240',
		'255.255.255.248',
		'255.255.255.252',
		'255.255.255.254',
		'255.255.255.255'
		]
	cidrs = ['/0','/1','/2','/3','/4','/5','/6','/7','/8','/9',
		'/10','/11','/12','/13','/14','/15','/16','/17','/18',
		'/19','/20','/21','/22','/23','/24','/25','/26','/27',
		'/28','/29','/30','/31','/32']

	index = masks.index(subnet)
	return cidrs[index]

def main():
	infile_path = '/Users/greatscott/Downloads/Allnetworks.csv'
	outfile_path = '/Users/greatscott/Downloads/vlan_andrew.csv'

	# create CSV that VLAN data will be written to
	outfile = open(outfile_path, 'a')
	writer = csv.writer(outfile)
	writer.writerow(['subnet','dept_code','upload_date']) # write headers

	infile = open(infile_path, 'rU')
	reader = csv.reader(infile)
	for row in reader:
		if('255' in row[1]):
		    subnet = row[0] + getCidr(row[0], row[1])
		else:
			subnet = row[0] + '/' + row[1]
		writer.writerow([subnet, row[2]])

if __name__ == '__main__':
	main()