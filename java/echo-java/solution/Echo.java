import java.util.Scanner;

public class Echo {
    public static void main(String[] args) {
        try (final Scanner scanner = new Scanner(System.in)) {
            // Read a sentence.
            final String sentence = scanner.nextLine();
            // Print the sentence.
            System.out.println(sentence);
        }
    }
}
