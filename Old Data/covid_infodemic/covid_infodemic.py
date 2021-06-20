import pandas as pd 
import csv

fake = pd.read_csv('./Old Data/covid_infodemic/covid_lies_fake.tsv', sep='\t', header=0)
true = pd.read_csv('./Old Data/covid_infodemic/covid_lies_true.tsv', sep='\t', header=0)
fake.to_csv('covid_lies_fake.csv', sep=',')
true.to_csv('covid_lies_true.csv', sep=',')

# tsv = pd.read_csv('covid19_infodemic_english_data.tsv', sep='\t', header=0)
# tweet_data = pd.read_csv('covid19_infodemic_tweet_data.tsv', sep='\t', header=0)


# fake = tsv[tsv['q1_label'] == 'yes']
# fake1 = fake[fake['q2_label'] == '5_yes_definitely_contains_false_info']
# fake2 = fake[fake['q2_label'] == '4_yes_probably_contains_false_info']
# fake3 = fake[fake['q2_label'] == '3_not_sure']
# fake = pd.concat([fake1, fake2, fake3])
# fake = tweet_data[tweet_data['id'].isin(fake['tweet_id'])]

# true = tsv[tsv['q1_label'] == 'yes']
# true1 = true[true['q2_label'] == '1_no_definitely_contains_no_false_info']
# true2 = true[true['q2_label'] == '2_no_probably_contains_no_false_info']
# true = pd.concat([true1, true2])
# true = tweet_data[tweet_data['id'].isin(true['tweet_id'])]

# fake.to_csv('covid_lies_fake.tsv', sep='\t')
# true.to_csv('covid_lies_true.tsv', sep='\t')

