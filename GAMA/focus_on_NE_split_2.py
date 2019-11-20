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
MGA_name = 'ne_focus_split_2' 
max_no_of_fit_individuals = 100
reps_of_unique_ko = 1

jr_ne_151_tuple = ('MG_120', 'MG_121', 'MG_122', 'MG_123', 'MG_127', 'MG_130', 'MG_132', 'MG_139', 'MG_143', 'MG_149', 'MG_170', 'MG_172', 'MG_183', 'MG_184', 'MG_186', 'MG_187', 'MG_188', 'MG_189', 'MG_190', 'MG_191', 'MG_192', 'MG_200', 'MG_205', 'MG_206', 'MG_208', 'MG_209', 'MG_210', 'MG_482', 'MG_213', 'MG_214', 'MG_217', 'MG_218', 'MG_225', 'MG_226', 'MG_227', 'MG_235', 'MG_236')
min_ko_size = 25
safe_min_ko_size = 15
max_ko_size = len(jr_ne_151_tuple)
safe_max_ko_size = len(jr_ne_151_tuple)
genetic_algorithm = GeneticAlgorithmFocusSet(min_ko_size, max_ko_size, safe_min_ko_size, safe_max_ko_size, jr_ne_151_tuple, dict_of_cluster_instances, dict_for_checkStop, MGA_name, max_no_of_fit_individuals, reps_of_unique_ko, generation_num_to_gen_size_dict = {0: 400, -1: 300}, mutation_probability = 0.4)
genetic_algorithm.run()
