int gcd(int a, int b) {
    while (b != 0) {
        int rest = a % b;
        a = b;
        b = rest;
    }
    return a;
}
