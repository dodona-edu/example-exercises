class Stack {
    private values: number[] = [];

    push(value: number): void {
        this.values.push(value);
    }

    pop(): number {
        return this.values.pop()!;
    }

    peek(): number {
        return this.values[this.values.length - 1];
    }

    size(): number {
        return this.values.length;
    }
}
