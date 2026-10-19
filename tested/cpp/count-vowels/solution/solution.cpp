#include <cctype>
#include <string>

int count_vowels(const std::string& text) {
    int count = 0;
    for (char c : text) {
        char lower = std::tolower(c);
        if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
            count++;
        }
    }
    return count;
}
