class Student {
    private String name;
    private int sum = 0;
    private int count = 0;

    public Student(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void addGrade(int grade) {
        sum += grade;
        count++;
    }

    public double average() {
        return (double) sum / count;
    }
}
