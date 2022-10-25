with open ('test1.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([])