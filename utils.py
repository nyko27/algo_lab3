def read_from_file(path):
    with open(path) as f:
        data_list = [int(number) for number in f.read().split()]
    if len(data_list) % 2 == 0 or len(data_list) < 3:
        print("Wrong amount of input items")
        exit()
    return data_list


def create_pairs(data):
    pairs_list = []
    for person_index in range(1, len(data), 2):
        pairs_list.append([data[person_index], data[person_index + 1]])
    return pairs_list


def move_pairs_to_clans(pairs_list):
    original_clans = []
    clans = list(pairs_list)
    for pair in pairs_list:
        for clan in clans:
            if set(pair) & set(clan) and pair != clan:
                clan.extend(pair)

    for clan in clans:
        for subsequence in clans:
            if set(subsequence).issubset(set(clan)) and subsequence != clan:
                clans.remove(subsequence)

    for clan in clans:
        if len(set(clan)) != len(clan):
            original_clans.append(list(set(clan)))
        else:
            original_clans.append(clan)
    return original_clans


def create_adjacency_list(clans):
    adj_dict = {}
    for clan in clans:
        for person_index in range(len(clan)):
            clan_copy = list(clan)
            clan_copy.pop(person_index)
            if clan[person_index] in adj_dict.keys():
                adj_dict[clan[person_index]].append(clan_copy)
            else:
                adj_dict.update({clan[person_index]: clan_copy})

    return adj_dict


def rebuild_adjacency_list(adjacency_list):
    new_adjacency_list = {}
    vertexes = adjacency_list.keys()
    for person in vertexes:
        for another_person in vertexes:
            if person == another_person or another_person in adjacency_list[person]:
                continue
            elif person in new_adjacency_list.keys():
                new_adjacency_list[person].append(another_person)
            else:
                new_adjacency_list.update({person: [another_person]})
    return new_adjacency_list


def count_possible_pairs(rebuilt_adjacency_list):
    pairs_count = 0
    dict_keys = rebuilt_adjacency_list.keys()
    for person in dict_keys:
        values = rebuilt_adjacency_list[person]
        for potential_pair in values:
            if potential_pair % 2 != person % 2:
                pairs_count += 1
    return int(pairs_count / 2)


def algorithm(data_path):
    return count_possible_pairs(
        rebuild_adjacency_list(create_adjacency_list(move_pairs_to_clans(create_pairs(read_from_file(data_path))))))
