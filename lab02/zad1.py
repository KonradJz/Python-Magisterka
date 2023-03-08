input_str = input("Podaj dane oddzielone separatorem: ")
source_sep = input("Podaj separator źródłowy: ")
target_sep = input("Podaj separator docelowy: ")

data_list = input_str.split(source_sep)
output_str = target_sep.join(data_list)

print("Wynik: ", output_str)