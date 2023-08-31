jumbled_superheroes = ["DocToR_sTRAngE", "sPidERmaN", "MoON_KnigHT", "caPTAIN_aMERIca", "hULK"]
indices = []
decoded_names = []

for index, name in enumerate(jumbled_superheroes):
    indices.append(index)
    decoded_name = name.lower().replace('_', ' ')
    decoded_names.append(decoded_name)

print("Indices:", indices)
print("Decoded Names:", decoded_names)



#decoded_names = ['doctor strange', 'spiderman', 'moon knight', 'captain america', 'hulk']

length_calculator = lambda x: len(x)
name_lengths = list(map(length_calculator, decoded_names))

print("Name Lengths:", name_lengths)



name_lengths = [14, 9, 11, 15, 4]
indices = [0, 1, 2, 3, 4]

indices.sort(key=lambda i: name_lengths[i])
print("Sorted Indices:", indices)



sorted_guest_list = [decoded_names[i].title() for i in indices]

print("Phase 5 kickoff list:")
for superhero in sorted_guest_list:
    print(superhero)
