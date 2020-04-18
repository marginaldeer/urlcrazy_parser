import csv
import sys


def dic_reader(urlcrazy_file):
    reader = csv.DictReader(urlcrazy_file)
    return reader


def dic_sorter(dict_reader):
    reged_dic = []
    avail_dic = []
    for line in dict_reader:

        # sanatize some things for easier usage
        line['typo_type'] = line.pop('Typo Type')
        line['dns_a'] = line.pop('DNS-A')
        line['country_a'] = line.pop('Country-A')
        line['dns_mx'] = line.pop('DNS-MX')
        line['cc_a'] = line.pop('CC-A')

        # sort them dics!
        if line['dns_a'] == '':
            avail_dic.append(line)
        elif line['dns_a'] == '104.219.49.163':
            avail_dic.append(line)
        else:
            reged_dic.append(line)

    # print(reged_dic)

    return avail_dic, reged_dic


if len(sys.argv) < 2:
    print("Usage: urlcrazy_parse.py file.csv")


with open(sys.argv[1]) as urlcrazy_file:
    new_dic = dic_reader(urlcrazy_file)
    result = dic_sorter(new_dic)
    avail_domains, reged_domains = result
    print('__Available Domains__')
    print('typo_type,typo,dns_a,dns_mx,country_a,extension')
    for line in avail_domains:
        print(line['typo_type'] + ',' + line['Typo'] + ',' + line['dns_a'] + ',' +
              line['dns_mx'] + ',' + line['country_a'] + ',' + line['Extn'])

    print()
    print()
    print('__Registered Domains__')
    print('typo_type,typo,dns_a,dns_mx,country_a,extension')
    for line in reged_domains:
        print(line['typo_type'] + ',' + line['Typo'] + ',' + line['dns_a'] + ',' +
              line['dns_mx'] + ',' + line['country_a'] + ',' + line['Extn'])
