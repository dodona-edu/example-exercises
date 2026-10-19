fun evenSquares(numbers: List<Int>): List<Int> {
    return numbers.filter { it % 2 == 0 }.map { it * it }
}
