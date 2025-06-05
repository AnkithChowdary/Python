friends=[
  {"name":"Suresh","Age":21},
  {"name":"Saurabh","Age":23},
  {"name":"Anne","Age":20}
]


print(friends[1]["name"])


student_attendance={"Rolf":96,"Bob":80,"Anne":100}

for student,attendance in student_attendance.items():
  print(f"{student}: {attendance}")
