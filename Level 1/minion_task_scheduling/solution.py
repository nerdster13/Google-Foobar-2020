def solution(data, n):
  if n == 0:
    print ""
    return
  new_schedule = []
  for num in data:
    if data.count(num) <= n:
      new_schedule.append(num)
  print ','.join(map(str,new_schedule))

