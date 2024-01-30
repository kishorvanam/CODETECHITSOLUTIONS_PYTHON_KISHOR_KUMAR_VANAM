import matplotlib.pyplot as plt
student_performance=["elcellent","good","average","poor"]
number_of_students = [10,30,12,5]
plt.pie(number_of_students,labels=student_performance)
plt.show()