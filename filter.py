# def filter_sort(filter_parms, dataset):
#     filtered_lists={}
#     for parms in filter_parms:

#         filtered_lists[parms]=[]= [item for item in dataset if item.startswith(parms)]
#         filtered_lists[parms].sort()

#         for item in dataset:
#             if item.startswith(parms):
#                 filtered_lists[parms].append(item)
#             filtered_lists[parms].sort()
#     return filtered_lists(dataset) 


# filtre_parms=["1","2","3","4","5",]
# dataset=["101","104", "444", "244", "2", "33","48","5435","6463"]

# result = filter_sort(filtre_parms,dataset)
# print(result)
def filter_sort(filter_params, dataset):
    filtered_lists = {}

    # Step 1: Filter and sort individual lists
    for param in filter_params:
        filtered_lists[param] = [item for item in dataset if item.startswith(param)]
        filtered_lists[param].sort()

    # Step 2: Combine all sorted lists into a single list and sort it
    combined_sorted_list = []
    for key in filter_params:
        combined_sorted_list.extend(filtered_lists[key])

    # Sort the combined list
    combined_sorted_list.sort()

    return combined_sorted_list

# Example usage
filter_params = ["1", "2", "3", "4",]
dataset = ["101", "104", "444", "244", "2", "33", "48", "5435", "6463"]

result = filter_sort(filter_params, dataset)
print(result)
