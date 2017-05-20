# in order to generate a (semi) personalized cover letter we need to input a few variables :

# company_name              : -cn
# company_street_address    : -ca
# company_city              : -cc
# company_state             : -cs
# company_zip_code          : -cz

# job_title                 : -t
# hiring_manager_name       : -mn
# hiring_manager_position   : -mp

# also, we need (but can generate) the following
# day_of_month
# month_of_year
# year

# example :
    # python3 cover_generator.py -t <job_title> -mn <hiring_manager_name> -mp <hiring_manager_position> -cn <company_name> -ca <company_street_address> -cc <company_city> -cs <company_state> -cz <company_zip_code>

    # python3 cover_generator.py -t Data Analytics Engineer -mn Dorothy Potterhaven -mp Hiring Manager -cn PACCAR -ca 381 Empire Street -cc Seattle -cs Washington -cz 98411

import sys, os
import collections

global company_name, company_street_address, company_city, company_state, company_zip_code, job_title, hiring_manager_name, hiring_manager_position

company_name = company_street_address = company_city = company_state = company_zip_code = job_title = hiring_manager_name = hiring_manager_position = None

# XXX test print XXX
# print(company_name, company_street_address)

# dictionary of meaningful tags for command line argument parsing
global tags_dict
tags_dict = collections.OrderedDict()
tags_dict['-cn'] = company_name
tags_dict['-ca'] = company_street_address
tags_dict['-cc'] = company_city
tags_dict['-cs'] = company_state
tags_dict['-cz'] = company_zip_code
tags_dict['-t'] = job_title
tags_dict['-mn'] = hiring_manager_name
tags_dict['-mp'] = hiring_manager_position

global var_names
var_names = collections.OrderedDict()
var_names['-cn'] = 'company name'
var_names['-ca'] = 'company street address'
var_names['-cc'] = 'company city'
var_names['-cs'] = 'company state'
var_names['-cz'] = 'company zip code'
var_names['-t'] = 'job title'
var_names['-mn'] = 'hiring manager name'
var_names['-mp'] = 'hiring manager position'


# global tags_index
# tags_index = collections.OrderedDict()
# tags_index['-cn'] = 0
# tags_index['-ca'] = 1
# tags_index['-cc'] = 2
# tags_index['-cs'] = 3
# tags_index['-cz'] = 4
# tags_index['-t']  = 5
# tags_index['-mn'] = 6
# tags_index['-mp'] = 7

# tags = {
#     '-cn' : company_name,
#     '-ca' : company_street_address,
#     '-cc' : company_city,
#     '-cs' : company_state,
#     '-cz' : company_zip_code,
#     '-t' : job_title,
#     '-mn' : hiring_manager_name,
#     '-mp' : hiring_manager_position
# }

# for x in tags_dict:
#     print(x, tags_dict[x])

# loop through the arguments provided by the user
for alpha in sys.argv:

    # for each argument, compare it to the list of tags to see if it exists
    for beta in tags_dict:
        if alpha == beta:
            # this exists in our record, so we need to find the
            # position of the pattern in the command line args array
            # then we'll build a string that's made up of all of the
            # array elements between the index of match that we've found
            # and the next tag
            string_builder = ''

            index_of_matching_tag = sys.argv.index(alpha)

            # XXX test print XXX
            # print('index of alpha : ', str(sys.argv.index(alpha)))
            # print('length of argv : ', str(len(sys.argv)))

            i = index_of_matching_tag+1
            while i < len(sys.argv):
                if '-' in sys.argv[i]:
                    break
                string_builder += sys.argv[i] + " "
                i+=1


            tags_dict[alpha] = string_builder
            # print('string builder : ', string_builder)

            # for x in sys.argv:
            #
            #     print(x)
            # print('found a matching tag', alpha, 'equals', beta



for x in tags_dict:
    if tags_dict[x] == None:
        pass
    else:
        print(var_names[x], ':', tags_dict[x])

    # print(x)


# if len(sys.argv)>=4:
#     if (sys.argv[1] == 'help'):
#
#         # if (sys.argv[1] == 'help'):
#         print('Usage : \n\t$ python3 unit-conv.py <number_of_units> <unit_type>\n\t$ python3 unit-conv.py 1024 bits\n')
#     else:
#         # try to parse user input for the number of bytes and unit type
#         try:
#             company_name = int(sys.argv[1])
#         except:
#             num_bytes = -1
#             print('Usage : \n\t$ python3 unit-conv.py <number_of_units> <unit_type>\n\t$ python3 unit-conv.py 1024 bits\n')
#             pass
#
# try:
#     if (isinstance(sys.argv[2], str)):
#         unit = sys.argv[2]
# except:
#     pass




# probs won't need this if the user passes in command line args
def get_input():
    print('enter company name')
    input_string = input()
    return input_string
