def converter(today):
    today_split = today.split('-')
    tsy = today_split[0]
    tsm = today_split[1]
    tsd = today_split[2]
    if tsm == '01':
        tsm = 'January'
    elif tsm == '02':
        tsm = 'February'
    elif tsm == '03':
        tsm = 'March'
    elif tsm == '04':
        tsm = 'April'
    elif tsm == '05':
        tsm = 'May'
    elif tsm == '06':
        tsm = 'June'
    elif tsm == '07':
        tsm = 'July'
    elif tsm == '08':
        tsm = 'August'
    elif tsm == '09':
        tsm = 'September'
    elif tsm =='10':
        tsm = 'October'
    elif tsm =='11':
        tsm = 'November'
    elif tsm == '12':
        tsm = 'December'
    target_date = str(tsd+ ' ' + tsm + ' ' + tsy)
    #print(target_date)
    return target_date