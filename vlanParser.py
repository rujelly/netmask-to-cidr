###############################################################################
# vlanParser.py
#
# Turns Allnetworks.csv into our lookup file. This description is intentionally
# vague b/c opsec. Get at me, haxers.
###############################################################################

import sys
import csv

def getCidrForSubnet(subnet_mask):
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

    if '.' not in subnet_mask: # some rows already have CIDR instead of a subnet mask
        cidr = '/' + subnet_mask
        return cidr
    else:
        index = masks.index(subnet_mask)
        cidr = cidrs[index]
        return cidr

def createCsvWithHeaders(outfile_path, header_list):
    outfile = open(outfile_path, 'a')
    writer = csv.writer(outfile)
    writer.writerow(header_list)
    return writer

def deleteAndsFrom(dept_code):
    dept_code = dept_code.replace(' and', ',')
    return dept_code

def writeRowWith(ip_address, subnet_mask, dept_code, comment, vlan, vrf, outfile_writer):
    cidr = getCidrForSubnet(subnet_mask)
    ip_with_cidr = ip_address + cidr
    outfile_writer.writerow([ip_with_cidr, dept_code, comment, vlan, vrf])

def main():
    infile_path = '/Users/greatscott/Downloads/Allnetworks.csv'
    outfile_path = '/Users/greatscott/Downloads/vlan_andrew.csv'

    outfile_writer = createCsvWithHeaders(outfile_path, ['subnet','dept_code','comments','VLAN','VRF','upload_date'])
    infile = open(infile_path, 'rU')
    infile_reader = csv.reader(infile)

    network_column_index = 0
    ip_column_index = 1
    subnet_column_index = 2
    comment_column_index = 8
    dept_code_column_index = 46
    vlan_column_index = 57
    vrf_column_index = 58

    for row in infile_reader:
        if 'header' in row[network_column_index]:
            pass
        elif 'ipv6' in row[network_column_index]:
            pass
        else:
            ip_address = row[ip_column_index]
            subnet_mask = row[subnet_column_index]
            comment = row[comment_column_index]
            dept_code = row[dept_code_column_index]
            dept_code = deleteAndsFrom(dept_code)
            try:
                vlan = row[vlan_column_index]
            except:
                pass
            try:
                vrf = row[vrf_column_index]
            except:
                pass
            writeRowWith(ip_address, subnet_mask, dept_code, comment, vlan, vrf, outfile_writer)

if __name__ == '__main__':
    main()