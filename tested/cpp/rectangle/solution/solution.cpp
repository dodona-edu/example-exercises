class Rectangle {
public:
    Rectangle(int width, int height) : width(width), height(height) {}

    int area() {
        return width * height;
    }

    int perimeter() {
        return 2 * (width + height);
    }

private:
    int width;
    int height;
};
