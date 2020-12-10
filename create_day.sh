# get the day count
# day is the file which contains the day counter eg. 7 will download for 7th day and it increases to 8
# REQUIRED:: file with name 'counter_file' is required
counter_file="day"
day_count=`cat $counter_file`

# prepare the day name
day_name=advent_$day_count

# make the directory as advent_{day}
mkdir $day_name
cd $day_name

# copy the template of the code
# REQUIRED:: file with name 'template' is required
template="template.py"
code_file="$day_name.py"
cp ../$template $code_file

# session information from the browser - cookies. (inspect -> network tab - Refresh the page - Cookies - session)
session="53616c7465645f5f74aac04fad93be99b2495499b8037851fdb2458b802a26ab37d74fdde2ccc509a0de938b69a9abf9"

# create inputs.txt
# this will download for the current day
input_file="inputs.txt"
curl https://adventofcode.com/2020/day/$day_count/input --cookie "session=$session" >> $input_file

#increment day counter and store in counter_file
a=`expr $day_count + 1`
echo $a > ../$counter_file

#print message
echo " Day $day_name successfully created."
