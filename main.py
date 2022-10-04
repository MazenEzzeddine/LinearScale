
import matplotlib.pyplot as plt
import csv

from numpy import double

def linearnonskewed():

    t5 = []
    t15 = []
    lamda15 = []
    lamda5 = []


    t1 = []
    lamda1 = []


    s15=0
    s5=0
    s1=0
    with open('LinearArrivalRate.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            #t.append(math.floor(double(row[0])))
            #t.append(str(row[0]))
            t15.append(s15)
            s15 +=5
            lamda15.append(double(row[1]))

    for r in range(len(t15)):
        print(r, t15[r])
    print(len(t15))

    with open('Linearconsumptionrate.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            #t.append(math.floor(double(row[0])))
            #t.append(str(row[0]))
            t1.append(s1)
            s1 +=5
            lamda1.append(double(row[1]))
    for r in range(len(t1)):
           print(r, t1[r])
           print(len(t1))
    with open('Linearreplicas.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            #t.append(math.floor(double(row[0])))
            #t.append(str(row[0]))
            t5.append(s5)
            s5 +=5
            lamda5.append(double(row[1]))
    for r in range(len(t5)):
           print(r, t5[r])
           print(len(t5))


    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    # ax1.plot(t5, lamda5, color='blue', label='arrival rate')
    # ax1.plot(t15, lamda15, color='red', label='consumption rate')
    # ax1.plot(t1, lamda1, color='black', label='Max consumption rate')
    rep = []
    for r in lamda5:
        var = r/95
        rep.append(var)


    ax1.plot(t5, lamda5)
    ax1.plot(t15, lamda15,  label='arrival rate')
    ax1.plot(t1, lamda1,  label='consumption rate')

    ax2.plot(t5, rep, 'r',  label='replicas')
    #
    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Arrival/consumption Rate')
    # #ax2.spines['left'].set_color('blue')
    # #ax2.spines['right'].set_color('red')
    #
    ax2.set_ylabel('Consumer replicas')
    #
    plt.title('Linear scale ')
    ax1.legend()
    ax2.legend(loc =4 )
    #
    plt.show()


def laglinearnonskewed():

    t5 = []
    t15 = []
    lamda15 = []
    lamda5 = []


    t1 = []
    lamda1 = []


    s15=0
    s5=0
    s1=0
    with open('LinearLag.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            #t.append(math.floor(double(row[0])))
            #t.append(str(row[0]))
            t15.append(s15)
            s15 +=5
            var = double(row[1])
            if var < 0:
             lamda15.append(0)
            else:
             lamda15.append(var)

    for r in range(len(t15)):
        print(r, t15[r])
    print(len(t15))

    # with open('consumptionrate.csv', 'r') as csvfile:
    #     plots = csv.reader(csvfile, delimiter=',')
    #     for row in plots:
    #         #t.append(math.floor(double(row[0])))
    #         #t.append(str(row[0]))
    #         t1.append(s1)
    #         s1 +=5
    #         lamda1.append(double(row[1]))
    # for r in range(len(t1)):
    #        print(r, t1[r])
    #        print(len(t1))
    # with open('replicas.csv', 'r') as csvfile:
    #     plots = csv.reader(csvfile, delimiter=',')
    #     for row in plots:
    #         #t.append(math.floor(double(row[0])))
    #         #t.append(str(row[0]))
    #         t5.append(s5)
    #         s5 +=5
    #         lamda5.append(double(row[1]))
    # for r in range(len(t5)):
    #        print(r, t5[r])
    #        print(len(t5))


    fig, ax1 = plt.subplots()
    # #ax2 = ax1.twinx()
    #ax1.plot(t5, lamda5, color='blue', label='lag')
    ax1.plot(t15, lamda15, color='red', label='Event Lag')
    # ax1.plot(t1, lamda1, color='black', label='workload1')

    # #ax2.plot(t, replicas, '--r',  label='replicas')
    #
    ax1.set_xlabel('Time (sec)')
    ax1.set_ylabel('Event Lag')
    # #ax2.spines['left'].set_color('blue')
    # #ax2.spines['right'].set_color('red')
    #
    # #ax2.set_ylabel('Consumer replicas')
    #
    plt.title('Event lag with Linear scale ')
    ax1.legend()
    # #ax2.legend(loc=1)
    #

    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    linearnonskewed()
    laglinearnonskewed()

