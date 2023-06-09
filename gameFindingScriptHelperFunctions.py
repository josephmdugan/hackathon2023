
# TTRPG Game Finding Script Helper Functions
# Caden Mcdonough, Joey Dugan

# Written 4/15/23 and 4/16/23 for the Cal Poly Humboldt Hackathon

class user:
  def __init__(self, username, time, age):
    self.username = username
    self.time = time
    self.age = age

class time_group:
  def __init__(self, time):
    self.time = time
    self.people = []
    self.length = 0


def open_file_and_clean_data(filename):
   f = open(filename, "r")
   data = f.readlines()
   f.close()

   cleanedData = []

   for i in range(6, len(data)):
      cleanedData += data[i].split(",")

   for i in range(len(cleanedData)):
      cleanedData[i] = cleanedData[i].replace('\"', '')
      cleanedData[i] = cleanedData[i].strip()
    
   return cleanedData

# def time_sort(times):
#   new_time_array = []
#   sun_far_index = 0
#   mon_far_index = 0
#   tue_far_index = 0
#   wed_far_index = 0
#   thur_far_index = 0
#   fri_far_index = 0
#   sat_far_index = 0
#   for i in range(len(times)):
#     if "Sunday" in times[i]:
#       new_time_array[sun_far_index] = times[i]
#       sun_far_index += 1
#     elif "Monday" in times[i]:
#        new_time_array[mon_far_index] = times[i]
#        mon_far_index += 1
#     elif "Tuesday" in times[i]:
#       new_time_array[tue_far_index] = times[i]
#       tue_far_index += 1
#     elif "Wednesday" in times[i]:
#       new_time_array[wed_far_index] = times[i]
#       wed_far_index += 1
#     elif "Thursday" in times[i]:
#       new_time_array[thur_far_index] = times[i]
#       thur_far_index += 1
#     elif "Friday" in times[i]:
#       new_time_array[fri_far_index] = times[i]
#       fri_far_index += 1
#     elif "Saturday" in times[i]:
#       new_time_array[sat_far_index] = times[i]
#       sat_far_index += 1
      
#     else:
#       pass
#     sun_far_index = 0
#     mon_far_index = sun_far_index + 1
#     tue_far_index = mon_far_index + 1
#     wed_far_index = tue_far_index + 1
#     thur_far_index = wed_far_index + 1
#     fri_far_index = thur_far_index + 1
#     sat_far_index = fri_far_index + 1
#   return new_time_array
     


def sort_users(users):
  time_groups = []
  inserted_times = []

  for i in range(len(users)):
      if users[i].time not in inserted_times:
        inserted_times.append(users[i].time)
        
  inserted_times.sort()

  for i in range(len(inserted_times)):
     time_groups.append(time_group(inserted_times[i]))

  users_added = []

  for i in range(len(users)):
      for j in range(len(time_groups)):
        if users[i].username not in users_added and users[i].time == time_groups[j].time and time_groups[j].length < 5:
            time_groups[j].people.insert(j, users[i].username)
            time_groups[j].length += 1
            users_added.append(users[i].username)
        elif (users[i].username not in users_added and users[i].time == time_groups[j].time and j == len(time_groups)):
            time_groups.insert(j, (time_group(users[i].time)))
            users_added.append(users[i].username)
            group_num = len(time_groups) -1
            time_groups[group_num].people.append(users[i].username)
        else:
            pass

  finished_cleaning = False
  i = 0
  while not finished_cleaning:
    if time_groups[i].people == []:
        del time_groups[i]
        i -= 1
    i += 1
    if i == len(time_groups):
        finished_cleaning = True
      
  return time_groups



def get_hour_minute(time):
    index = 0
    for i in range(len(time)):
      if time[i] == ":":
        index = i
    hour = int(time[:index])
    minute = time[index+1:]
    
    if minute != "00":
       hour += 1
       hour = hour%24
       minute = "00"
    
    return str(hour)

def create_group_string(time_groups):
  groups = ""
  for i in range(len(time_groups)):
        groups += "Group " + str(i) + ": " + time_groups[i].time + ":00, " + str(time_groups[i].people) + "\n"

  return groups

def concatenate_age_groups(group1, group2, group3, group4):
  groups = ""

  groups += "Groups Under 18: \n"
  groups += group1

  groups += "\n\n"
  groups += "Groups Over 18, but under 30: \n"
  groups += group2

  groups += "\n\n"
  groups += "Groups Over 30, but under 60: \n"
  groups += group3

  groups += "\n\n"
  groups += "Groups Over 60: \n"
  groups += group4

  return groups
