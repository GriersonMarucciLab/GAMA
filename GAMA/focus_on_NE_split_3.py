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
MGA_name = 'ne_focus_split_3' 
max_no_of_fit_individuals = 100
reps_of_unique_ko = 1

jr_ne_151_tuple = ('MG_239', 'MG_240', 'MG_244', 'MG_252', 'MG_259', 'MG_262', 'MG_498', 'MG_264', 'MG_265', 'MG_277', 'MG_288', 'MG_289', 'MG_290', 'MG_291', 'MG_293', 'MG_297', 'MG_298', 'MG_305', 'MG_309', 'MG_310', 'MG_312', 'MG_316', 'MG_317', 'MG_318', 'MG_324', 'MG_327', 'MG_329', 'MG_333', 'MG_335', 'MG_336', 'MG_339', 'MG_344', 'MG_346', 'MG_349', 'MG_352', 'MG_353', 'MG_355', 'MG_356')
min_ko_size = 25
safe_min_ko_size = 15
max_ko_size = len(jr_ne_151_tuple)
safe_max_ko_size = len(jr_ne_151_tuple)
genetic_algorithm = GeneticAlgorithmFocusSet(min_ko_size, max_ko_size, safe_min_ko_size, safe_max_ko_size, jr_ne_151_tuple, dict_of_cluster_instances, dict_for_checkStop, MGA_name, max_no_of_fit_individuals, reps_of_unique_ko, generation_num_to_gen_size_dict = {0: 400, -1: 300}, mutation_probability = 0.4)
genetic_algorithm.run()
