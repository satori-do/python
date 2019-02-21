exam_st_date = (('https://192.168.33.19',),)

# Sample Output : The examination will start from : 11 / 12 / 2014

newtup = str(exam_st_date).replace("(", "")
newtup1 = str(newtup).replace("'", "")
newtup2 = str(newtup1).replace(",", "")
newtup3 = str(newtup2).replace(")", "")



print(newtup3)
