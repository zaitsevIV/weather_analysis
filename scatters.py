from file_analysis import received_data

max_of_TMax_index = [i for i, ltr in enumerate(received_data['TMax']) if ltr == max(received_data['TMax'])]
min_of_TMax_index = [i for i, ltr in enumerate(received_data['TMax']) if ltr == min(received_data['TMax'])]
max_of_TMin_index = [i for i, ltr in enumerate(received_data['TMin']) if ltr == max(received_data['TMin'])]
min_of_TMin_index = [i for i, ltr in enumerate(received_data['TMin']) if ltr == min(received_data['TMin'])]
