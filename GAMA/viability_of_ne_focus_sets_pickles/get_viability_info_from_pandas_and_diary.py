import glob
import pandas as pd
def getViability(path_to_sims):
	data_dict = {'division_time': (), 'average_growth_rate': ()}
	indexs = ()
	counter = 1
	pickle_path_list = glob.glob(path_to_sims + '/**/basic_summary*.pickle', recursive=True)
	print('pickle_path_list = ', pickle_path_list)
	for pickle_path in glob.iglob(path_to_sims + '/**/basic_summary*.pickle', recursive=True):
		print('pickle_path = ', pickle_path)
		print('Attempting step: ', counter)
		basic_summary = pd.io.pickle.read_pickle(pickle_path)
		growth_mean = basic_summary['metabolicReaction_growth'].mean()
		pinch_data = basic_summary['geometry_pinchedDiameter']
		pinched_times = list(pinch_data[pinch_data == 0].index)
		first_pinch = (pinched_times[0] if pinched_times else 0)
		data_dict['division_time'] += (first_pinch,)
		data_dict['average_growth_rate'] += (growth_mean,)
		indexs += (pickle_path,)
		counter += 1

	viability_df = pd.DataFrame(data_dict)
	viability_df.index = indexs

	return viability_df
