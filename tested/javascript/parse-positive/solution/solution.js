function parsePositive(text) {
    const number = Number(text);
    if (!Number.isInteger(number) || number <= 0) {
        throw new Error("not a positive number");
    }
    return number;
}
