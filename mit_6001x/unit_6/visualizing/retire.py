import pylab as plt


def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    m_rate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + m_rate) + monthly]
    return base, savings


def display_retire_w_monthlies(monthlies, rate, terms):
    plt.figure("retire Month")
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label="retire:" + str(monthly))
        plt.legend(loc="upper left")
    plt.show()


display_retire_w_monthlies([500, 600, 700, 800, 900, 1000, 1100], 0.05, 40 * 12)
