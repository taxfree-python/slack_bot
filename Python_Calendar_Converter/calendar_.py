import calendar as cal
import sys

args = sys.argv

convert_target_day = args[1]
#print(convert_target_day)
convert_target_month = args[2]
#print(convert_target_month)
convert_target_year = args[3]
#print(convert_target_year)
convert_target_str = str(convert_target_day + " " + convert_target_month + " " + convert_target_year)
print(convert_target_str)
date_to_convert = cal.Calendar().to_french_revolutionary(convert_target_str)

print(date_to_convert)