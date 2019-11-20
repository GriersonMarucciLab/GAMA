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
MGA_name = 'ne_focus_split_4' 
max_no_of_fit_individuals = 100
reps_of_unique_ko = 1

jr_ne_151_tuple = ('MG_358', 'MG_359', 'MG_369', 'MG_370', 'MG_376', 'MG_380', 'MG_385', 'MG_386', 'MG_390', 'MG_391', 'MG_392', 'MG_393', 'MG_398', 'MG_399', 'MG_401', 'MG_402', 'MG_403', 'MG_404', 'MG_405', 'MG_408', 'MG_409', 'MG_410', 'MG_411', 'MG_412', 'MG_421', 'MG_425', 'MG_427', 'MG_428', 'MG_438', 'MG_442', 'MG_447', 'MG_448', 'MG_454', 'MG_457', 'MG_460', 'MG_463', 'MG_464', 'MG_467', 'MG_468', 'MG_526')
min_ko_size = 25
safe_min_ko_size = 15
max_ko_size = len(jr_ne_151_tuple)
safe_max_ko_size = len(jr_ne_151_tuple)
genetic_algorithm = GeneticAlgorithmFocusSet(min_ko_size, max_ko_size, safe_min_ko_size, safe_max_ko_size, jr_ne_151_tuple, dict_of_cluster_instances, dict_for_checkStop, MGA_name, max_no_of_fit_individuals, reps_of_unique_ko, generation_num_to_gen_size_dict = {0: 400, -1: 300}, mutation_probability = 0.4)
genetic_algorithm.run()
