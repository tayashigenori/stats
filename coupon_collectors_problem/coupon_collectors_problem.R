# compute Coupon collector's problem
# E[n] = n * Hn
#      = n * (1/1 + 1/2 + ... + 1/n)

N <- 100
x <- seq(0,N)

# ‰Šú‰»
E_list <- as.list(NULL)
hn_list <- as.list(NULL)

for (n in x) {
    if (n == 0) {
        hn <- 0
        E <- 0
    } else {
        hn <- sum( 1/seq(n) )
        E <- n * hn
    }
    hn_list <- append(hn_list, hn)
    E_list <- append(E_list, E)
}

plot(x, hn_list, ylim=c(1,E), ylab="")
par(new=T)
plot(x, E_list, ylim=c(1,E), ylab="")
