def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one$
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    for row in reader: 
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        # If this date is smaller than the one we're looking for,
        # we skip this row
        if row_date < start_date:
            continue

        # If this date is smaller than the current minimum,
        # we pick it as the new minimum, resetting the list of
        # employees at the minimal date.
        if row_date < min_date:
            min_date = row_date
            min_date_employees = []

        # If this date is the same as the current minimum,
        # we add the employee in this row to the list of
        # employees at the minimal date.
        if row_date == min_date:
            min_date_employees.append("{} {}".format(row[0], row[1]))

    return min_date, min_date_employees
