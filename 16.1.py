# # 16.1 task//1 
# member_ids = ["GYM101", "GYM102", "GYM103", "GYM104", "GYM105", "GYM106"]


# it = iter(member_ids)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# result = next(it, "END")
# print(result)
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> & 'C:\Program Files\Python314\python.exe' '"c:/tops/session 1/16.1.py"'
# GYM101
# GYM102
# GYM103
# GYM104
# GYM105
# GYM106
# END

# # 16.2 task//2
# names = ["Aarav", "Priya", "Rohan", "Neha", "Kabir", "Ananya"]
# plans = ["Monthly", "Quarterly", "Yearly", "Monthly", "Yearly", "Quarterly"]
# fees = [1500, 4000, 12000, 1500, 12000, 4000]


# for num, (name, plan, fee) in enumerate(zip(names, plans, fees), start=1):
#   print(f"{num}. {name} - {plan} - Rs {fee}")

# fee_dict = dict(zip(names, fees))
# print("\nFee Dictionary:", fee_dict)

# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> & 'C:\Program Files\Python314\python.exe' '"c:/tops/session 1/16.1.py"'
# 1. Aarav - Monthly - Rs 1500
# 2. Priya - Quarterly - Rs 4000
# 3. Rohan - Yearly - Rs 12000
# 4. Neha - Monthly - Rs 1500
# 5. Kabir - Yearly - Rs 12000
# 6. Ananya - Quarterly - Rs 4000

# Fee Dictionary: {'Aarav': 1500, 'Priya': 4000, 'Rohan': 12000, 'Neha': 1500, 'Kabir': 12000, 'Ananya': 4000}
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> 

# 14.3 task 3
# def daily_checkins(days):
#   for day in range(1, days + 1):
#     count = 40 + (day * 7) % 25
#     yield count

# checkins = daily_checkins(14)

# d1 = next(checkins)
# d2 = next(checkins)
# d3 = next(checkins)

# print("Day 1:", d1)
# print("Day 2:", d2)
# print("Day 3:", d3)


# total = d1 + d2 + d3

# for count in checkins:
#   print("Next day check-in:", count)
#   total = total + count

# print("Total 14-day check-ins:", total)
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> & 'C:\Program Files\Python314\python.exe' '"c:/tops/session 1/16.1.py"'
# Day 1: 47
# Day 2: 54
# Day 3: 61
# Next day check-in: 43
# Next day check-in: 50
# Next day check-in: 57
# Next day check-in: 64
# Next day check-in: 46
# Next day check-in: 53
# Next day check-in: 60
# Next day check-in: 42
# Next day check-in: 49
# Next day check-in: 56
# Next day check-in: 63
# Total 14-day check-ins: 745

# 1. 8 मेंबर्स की डिक्शनरी वाली लिस्ट बनाना
members = [
    {"name": "Aarav", "days_left": 5},
    {"name": "Priya", "days_left": 20},
    {"name": "Rohan", "days_left": 2},
    {"name": "Neha", "days_left": 15},
    {"name": "Kabir", "days_left": 7},
    {"name": "Ananya", "days_left": 30},
    {"name": "Vikram", "days_left": 0},
    {"name": "Meera", "days_left": 12},
]


# 2. जेनरेटर फंक्शन जो सिर्फ 7 या उससे कम दिन बचे होने पर अलर्ट दे
def renewal_alerts(member_list):
  for m in member_list:
    if m["days_left"] <= 7:
      yield f"Alert: {m['name']}'s plan expires in {m['days_left']} days!"


# 3. जेनरेटर ऑब्जेक्ट बनाना और प्रिंट करना
alerts = renewal_alerts(members)
print("Generator object:", alerts)

# 4. लूप चलाकर अलर्ट प्रिंट करना और गिनना
alert_count = 0
for msg in alerts:
  print(msg)
  alert_count = alert_count + 1

print("Total alerts yielded:", alert_count)
