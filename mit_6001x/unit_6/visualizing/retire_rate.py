import pylab as plt


def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    m_rate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + m_rate) + monthly]
    return base, savings


def display_retire_w_monthlies(monthlies, rates, terms):
    plt.figure("retire Both")
    plt.clf()
    plt.xlim(30 * 13, 40 * 12)
    month_labels = ["r", "b", "g", "k"]
    rate_labels = ["-", "o", "--"]
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        month_label = month_labels[i % len(month_labels)]
        for j in range(len(rates)):
            rate = rates[j]
            rate_label = rate_labels[j % len(rate_labels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(
                xvals,
                yvals,
                month_label + rate_label,
                label="retire:" + str(monthly) + ":" + str(int(rate * 100)),
            )
            plt.legend(loc="upper left")
    plt.show()


display_retire_w_monthlies([500, 700, 900, 1100], [0.03, 0.05, 0.07], 40 * 12)
