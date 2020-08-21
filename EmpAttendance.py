import EmpAttendanceRecord as er
import os.path as path


Emp_records = er.AttnRecord()


count = 0

if not path.exists("outputPS5.txt"):
    output = open("outputPS5.txt", "w+")
else:
    output = open("outputPS5.txt", "w+")

inputps5afile = open("inputPS5.txt", 'r')
for i in inputps5afile:
    removal_list = [' ', '\t', '\n']
    for s in removal_list:
        i = i.replace(s, '')

    EmpId = int(i)

    print("********Registering Employee EmpId:- " , EmpId)

    Emp_records.recordSwipeRec(EmpId)
    count += 1

#print("starting heap sort for employee list " + str(Emp_records.employee))

output.write("Total number of employees recorded today: " + str(Emp_records.getSwipeRec(Emp_records.tail)-1) + "\n")

print(" Reading from promptsPS5.txt")
input_promptsPS5= open("promptsPS5.txt", "r")
for i in input_promptsPS5:
    print("value of i after trimming spaces is " + i)
    if i == "onPremises:" :
        employeeOnPremise = Emp_records.onPremisesRec(Emp_records.tail) - 1
        if employeeOnPremise == 0:
            output.write("No employees present on premises.\n")
        else:
            output.write(str(employeeOnPremise) + " employees still on premises.\n")
    elif i[0:8] == "checkEmp":
        print("*************Check for Emplyee presence*******************")
        EMPid = int(i.split(":")[1])
        print ("Emp ID is " , EMPid)
        employeeChk = Emp_records.checkEmpRec(Emp_records.tail, EMPid)
        print ("value of employeeChk is " , employeeChk )
        msg=""
        if employeeChk > 0:
            if employeeChk % 2 == 0:
                print("Employee id " + str(EMPid) + " swiped " + str(employeeChk) +
                             " times today and is currently outside office\n")
                #output.write("Employee id " + str(EMPid) + " swiped " + str(employeeChk) + " times today and is currently outside office\n")
                msg="Employee id " + str(EMPid) + " swiped " + str(employeeChk) + " times today and is currently outside office\n"
            else:
                print("Employee id "+ str(EMPid) + " swiped " + str(employeeChk) +
                             " times today and is currently in office\n")
                msg = "Employee id "+ str(EMPid) + " swiped " + str(employeeChk) + " times today and is currently in office\n"
                #output.write("Employee id "+ str(EMPid) + " swiped " + str(employeeChk) +
                            # " times today and is currently in office\n")
        else:
            print("Employee id "+ str(EMPid) + " did not swipe today.\n")
            msg= "Employee id "+ str(EMPid) + " did not swipe today.\n"
        output.write(msg)

    elif i[0:9] == "freqVisit":
        print("*************Check for visit count*******************")
        visitcount = int(i.split(":")[1])
        print("visitcount variable is ", visitcount)
        msg2=""
        #print("visitcount is ", visitcount)
        #print(Emp_records.frequentVisitorRec(Emp_records.tail, visitcount))
        visit_list=Emp_records.frequentVisitorRec(Emp_records.tail, visitcount)
        print("visit_list came out as", visit_list )
        if len(visit_list) == 0:
            msg2 = "No Employees swiped more than " + str(visitcount )+ " number of times today\n"
        else:
            msg2 = "Employees swiped more than " + str(visitcount) + " number of times today are:\n"
            for v in visit_list:
                msg2 = msg2 + str(v[0]) + "," + str(v[1]) + "\n" # "times")#.split(","))#[0], "swipe count is ", v.split(",")[1])

        output.write(msg2)

    elif i[0:5] == "range":
        print("*************Check for range*******************")
        lbound = i.split(":")[1]
        ubound = i.split(":")[2]
        msg4 = "Range: " + lbound + " to " + ubound + "\n"
        for j in range(0,len(Emp_records.employee)-1,1):
            print("value of j is ", j)
            #print ("value of EMPid at " , i, " is ", Emp_records.employee[i])

            if Emp_records.employee[j] in range(int(lbound),int(ubound)) :
                swipeCount = Emp_records.find_employee(Emp_records.employee[j]).attCtr
                if  swipeCount % 2 == 0:
                    presence_status = "out"
                else:
                    presence_status = "in"
                #print("employee id ", Emp_records.employee[i] , " is having swipe count as ",  ,"\n")
                msg4 = msg4 + str(Emp_records.employee[j]) + "," + str(swipeCount) + "," + str(presence_status) + "\n"
        output.write(msg4)
output.close()