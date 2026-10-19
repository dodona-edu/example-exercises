class Temperature {
    private double celsius;

    public Temperature(double celsius) {
        if (celsius < -273.15) {
            throw new IllegalArgumentException("below absolute zero");
        }
        this.celsius = celsius;
    }

    public double toFahrenheit() {
        return celsius * 9 / 5 + 32;
    }
}
