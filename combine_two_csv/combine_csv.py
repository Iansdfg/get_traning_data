import csv

def get_dic_and_keys():
    id_to_length = dict()
    id_list = []
    with open('video_len.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count+=1
                continue
            # print(row)
            video_id, video_duration = row[0], row[1]
            id_to_length[video_id] = video_duration
            id_list.append(video_id)

    return id_to_length, id_list


id_to_length, id_list = get_dic_and_keys()

id_to_times = dict()
for id_ in id_list:
    time_to_data = dict()
    id_to_times[id_] = time_to_data
    seconds = id_to_length[id_]
    for second in range(int(seconds)):
        # print(id_)
        time_to_data[second] = {
                'id': id_,
                'time': second,
                # senti
                'score_val':0,
                'score_max':0,
                'score_min':0,
                'score_avg':0,
                'score_std':0,
                'sentence':0,
                # facial
                'smile':0,
                'gender':0,
                'anger':0,
                'contempt':0,
                'disgust':0,
                'fear':0,
                'happiness':0,
                'neutral':0,
                'sadness':0,
                'surprise':0,
                'facial_type':0,
                # tag
                'tag_video_labe':0,
                'tag_video_type':0,
        }

# print(id_to_times['sad_3'])
# for key in id_to_times:
#     # print(key,id_to_times[key])
#     for sec_key in id_to_times[key]:
#         print(key,sec_key )

with open('get_senti_csv.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in readCSV:
        if count == 0:
            count+=1
            continue
        senti_time = int(row[0])
        senti_id = row[1]
        senti_val = row[2]
        senti_max = row[3]
        senti_min = row[4]
        senti_avg = row[5]
        senti_std = row[6]
        sentence  = row[7]

        id_to_times[senti_id][senti_time-1]['score_val'] = senti_val
        id_to_times[senti_id][senti_time-1]['score_max'] = senti_max
        id_to_times[senti_id][senti_time-1]['score_min'] = senti_min
        id_to_times[senti_id][senti_time-1]['score_avg'] = senti_avg
        id_to_times[senti_id][senti_time-1]['score_std'] = senti_std
        id_to_times[senti_id][senti_time-1]['sentence'] = sentence

        # print(id_to_times[senti_id][senti_time-1])
        
with open('tag_video_to_csv.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in readCSV:
        if count == 0:
            count+=1
            continue
        # print(row)
        faical_time = int(row[11])
        faical_id = row[0]
        # facial
        smile = row[1]
        gender = row[2]
        anger = row[3]
        contempt = row[4]
        disgust = row[5]
        fear = row[6]
        happiness = row[7]
        neutral = row[8]
        sadness = row[9]
        surprise = row[10]
        facial_type = row[12]
        # tag
        tag_video_labe = row[-2]
        tag_video_type = row[-1]


        id_to_times[faical_id][faical_time-1]['smile'] = smile
        id_to_times[faical_id][faical_time-1]['gender'] = gender
        id_to_times[faical_id][faical_time-1]['anger'] = anger
        id_to_times[faical_id][faical_time-1]['contempt'] = contempt
        id_to_times[faical_id][faical_time-1]['disgust'] = disgust
        id_to_times[faical_id][faical_time-1]['fear'] = fear
        id_to_times[faical_id][faical_time-1]['happiness'] = happiness
        id_to_times[faical_id][faical_time-1]['neutral'] = neutral
        id_to_times[faical_id][faical_time-1]['sadness'] = sadness
        id_to_times[faical_id][faical_time-1]['surprise'] = surprise
        id_to_times[faical_id][faical_time-1]['facial_type'] = facial_type
        id_to_times[faical_id][faical_time-1]['tag_video_labe'] = tag_video_labe
        id_to_times[faical_id][faical_time-1]['tag_video_type'] = tag_video_type

        # print(id_to_times[faical_id][faical_time-1])


res = []
# print(id_to_times['sad_3'])
for key in id_to_times:
    # print(key,id_to_times[key])
    for sec_key in id_to_times[key]:
        # print(key,sec_key, id_to_times[key][sec_key] )
        # print(id_to_times[key][sec_key])
        res.append(id_to_times[key][sec_key])

for row in res:
    print(row)


# for key_id in id_to_times:
#     for key_sec in time_to_data:
#         time_to_data[key_sec]['id'] = key_id
#         # print(key_id, key_sec, time_to_data[key_sec])
#         data = {
#                 'id': key_id,
#                 'time': time_to_data[key_sec]['time'],
#                 # senti
#                 'score_val':time_to_data[key_sec]['score_val'],
#                 'score_max':time_to_data[key_sec]['score_max'],
#                 'score_min':time_to_data[key_sec]['score_min'],
#                 'score_avg':time_to_data[key_sec]['score_avg'],
#                 'score_std':time_to_data[key_sec]['score_std'],
#                 'sentence':time_to_data[key_sec]['sentence'],
#                 # facial
#                 'smile':time_to_data[key_sec]['smile'],
#                 'gender':time_to_data[key_sec]['gender'],
#                 'anger':time_to_data[key_sec]['anger'],
#                 'contempt':time_to_data[key_sec]['contempt'],
#                 'disgust':time_to_data[key_sec]['disgust'],
#                 'fear':time_to_data[key_sec]['fear'],
#                 'happiness':time_to_data[key_sec]['happiness'],
#                 'neutral':time_to_data[key_sec]['neutral'],
#                 'sadness':time_to_data[key_sec]['sadness'],
#                 'surprise':time_to_data[key_sec]['surprise'],
#                 'facial_type':time_to_data[key_sec]['facial_type'],
#                 # tag
#                 'tag_video_labe':time_to_data[key_sec]['tag_video_labe'],
#                 'tag_video_type':time_to_data[key_sec]['tag_video_type'],
#         }
#         # print(data)
#         res.append(data)
        

# for row in res:
#     print(row)

csv_columns = [
    'id',
    'time',
    # senti
    'score_val',
    'score_max',
    'score_min',
    'score_avg',
    'score_std',
    'sentence',
    # facial
    'smile',
    'gender',
    'anger',
    'contempt',
    'disgust',
    'fear',
    'happiness',
    'neutral',
    'sadness',
    'surprise',
    'facial_type',
    # tag
    'tag_video_labe',
    'tag_video_type',
]
csv_file = "Names.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = csv_columns)
        writer.writeheader()
        for data in res:
            writer.writerow(data)
except IOError:
    print("I/O error") 



# if __name__ == "__main__":
#     creat_CSV_with_id_and_time()



