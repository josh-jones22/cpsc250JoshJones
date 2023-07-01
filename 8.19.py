contact_entry = input().strip()
indi_person = contact_entry.split(" ")
n_search = input().strip()
lst = {}
for i in indi_person:
    name_number = i.split(',')
    lst.update({name_number[0]: name_number[1]})

if n_search in lst:
    print(lst[n_search])