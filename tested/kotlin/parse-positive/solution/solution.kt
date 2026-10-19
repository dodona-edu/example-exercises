fun parsePositive(text: String): Int {
    val number = text.toIntOrNull()
    require(number != null && number > 0) { "not a positive number" }
    return number
}
