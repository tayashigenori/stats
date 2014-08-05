# compute Coupon collector's problem
# E[n] = n * Hn
#      = n * (1/1 + 1/2 + ... + 1/n)

N <- 100
x <- seq(0,N)

E_list <- 0
hn_list <- 0
for (n in 1:N) {
    hn <- sum( 1/seq(n) )
    hn_list <- append(hn_list, hn)
    E <- n * hn
    E_list <- append(E_list, E)
}

#plot(x, hn_list)
plot(x, E_list)
