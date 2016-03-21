import sys
import csv
from os import listdir

'''def parseFile(filename):
	"""
	Parse chunk of VLAN file for device data
	Args:
		File to be parsed
	Returns:
		2D list of VLAN data (each item = list of a single VLAN's data)
	"""

	device = []
	vlanFile = open(filename)

	# group file lines according to VLAN, and parse each VLAN
	vlanList = vlanFile.read().split('!')
	for sublist in vlanList:
		sublist = sublist.split('\n')
		device.append(parseVlan(sublist))

	return device'''

'''def parseVlan(sublist):
	"""
	Args:
		List of data for a single VLAN
	Returns:
		Dict of VLAN data
	"""
	vlan = dict(
		NAME 			= 0,
		DESCRIPTION 	= 0,
		IP_SUBNET_COMBOS = []
	)

	for line in sublist:
		if 'Vlan' in line:					# get VLAN name
			line = line.split(" ")
			name = line[1].strip()
			vlan['NAME'] = name[4:]
			print("VLAN found:\t" + vlan['NAME'])
		elif 'description' in line:			# get VLAN description
			line = line.split(" ")
			if 'name' not in line:
				vlan['DESCRIPTION'] = line[2].strip()
			else:
				vlan['DESCRIPTION'] = line[3].strip()
		elif '.' in line:					# get ip address, subnet, and description
			line = line.split(" ")
			print(line)
			try:							# strip items if there are any
				line[3] = line[3].strip()
				line[4] = line[4].strip()
				line[5] = line[5].strip()
			except:
				pass
			vlan['IP_SUBNET_COMBOS'].append(' '.join(line[3:5]))

	return vlan'''

'''def writeVLANToCSV(writer, vlan, filename):
	"""
	Args:
		List of data for a single device
		Dict of VLAN data to be written to CSV
		String of device name to write to CSV
	"""
	deviceName = filename[28:-4]

	# split ip and subnet and write one row per ip/subnet combo
	for each in vlan['IP_SUBNET_COMBOS']:
		each = each.split(" ")
		if(len(each) > 1): # if there's a subnet, convert IP to CIDR
			try:
				each[0] += getCIDR(each[0], each[1])
			except:
				pass
		temp = [deviceName, vlan['DESCRIPTION'], vlan['NAME']]
		temp.extend(each) # "each" is separate in case there is no subnet
		writer.writerow(temp)'''

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
			subnet = row[0] + row[1]
		writer.writerow([subnet, row[2]])

	'''# parse each file for vlan data and write to CSV
	for filename in filenames:
		print('Parsing \'' + filename + '\'')
		filename = PATH + '/' + filename
		device = parseFile(filename)
		for vlan in device:
			if vlan['NAME'] == 0 or vlan['DESCRIPTION'] == 0:	# some empty vlans will be in list
				pass											# don't write them to CSV
			else:
				writeVLANToCSV(writer, vlan, filename)
	print('CSV saved.')'''


if __name__ == '__main__':
	main()