#include <stdexcept>
#include <string>

int parse_positive(const std::string& text) {
    try {
        size_t used = 0;
        int number = std::stoi(text, &used);
        if (used == text.size() && number > 0) {
            return number;
        }
    } catch (const std::exception&) {
    }
    throw std::invalid_argument("not a positive number");
}
