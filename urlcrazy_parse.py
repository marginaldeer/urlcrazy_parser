import csv
import sys

def dic_reader(urlcrazy_file):
    reader = csv.DictReader(urlcrazy_file)
    return reader

def dic_sorter(dict_reader):
    reged_dic = []
    avail_dic = []
    for line in dict_reader:

        #sanatize some things for easier usage
        line['typo_type'] = line.pop('Typo Type')
        line['dns_a'] = line.pop('DNS-A')
        line['country_a'] = line.pop('Country-A')
        line['dns_mx'] = line.pop('DNS-MX')
        line['cc_a'] = line.pop('CC-A')

        #sort them dics!
        if line['dns_a'] == '':
            avail_dic.append(line)
        else:
            reged_dic.append(line)
    
    #print(reged_dic)

    return avail_dic, reged_dic




with open(sys.argv[1]) as urlcrazy_file:
    new_dic = dic_reader(urlcrazy_file)
    result = dic_sorter(new_dic)
    avail_domains, reged_domains = result
    print('__Available Domains__')
    for line in avail_domains:
        print(line)

    print()
    print()
    print('__Registered Domains__')
    for line in reged_domains:
        print(line)

