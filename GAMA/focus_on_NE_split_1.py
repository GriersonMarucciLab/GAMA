from multigeneration_algorithm import GeneticAlgorithmFocusSet
from connections import Bg

# declare all variables needed
cluster_user_name = 'oc13378'
ssh_config_alias = 'bg'
path_to_key = '/users/oc13378/.ssh/uob/uob-rsa'
name1 = 'Oliver'
name2 = 'Chalkley'
email = 'o.chalkley@bristol.ac.uk'
bg_connection = Bg(cluster_user_name, ssh_config_alias, path_to_key, name1, name2, email)
dict_of_cluster_instances = {'bg': bg_connection}
dict_for_checkStop = {'max_generation': [100]} 
MGA_name = 'ne_focus_split_1' 
max_no_of_fit_individuals = 100
reps_of_unique_ko = 1

jr_ne_151_tuple = ('MG_009', 'MG_012', 'MG_014', 'MG_015', 'MG_020', 'MG_027', 'MG_029', 'MG_030', 'MG_033', 'MG_039', 'MG_040', 'MG_046', 'MG_048', 'MG_050', 'MG_052', 'MG_055', 'MG_059', 'MG_061', 'MG_062', 'MG_063', 'MG_064', 'MG_065', 'MG_072', 'MG_073', 'MG_075', 'MG_083', 'MG_085', 'MG_086', 'MG_097', 'MG_101', 'MG_476', 'MG_104', 'MG_105', 'MG_109', 'MG_110', 'MG_119')

min_ko_size = 25
safe_min_ko_size = 15
max_ko_size = len(jr_ne_151_tuple)
safe_max_ko_size = len(jr_ne_151_tuple)
genetic_algorithm = GeneticAlgorithmFocusSet(min_ko_size, max_ko_size, safe_min_ko_size, safe_max_ko_size, jr_ne_151_tuple, dict_of_cluster_instances, dict_for_checkStop, MGA_name, max_no_of_fit_individuals, reps_of_unique_ko, generation_num_to_gen_size_dict = {0: 400, -1: 300}, mutation_probability = 0.4)
genetic_algorithm.run()
