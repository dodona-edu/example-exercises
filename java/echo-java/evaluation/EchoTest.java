import dodona.util.Interactive;
import org.junit.Assert;
import org.junit.Rule;
import org.junit.Test;

public class EchoTest {
    @Rule
    public final Interactive interactive = Interactive.forClass(Echo.class);

    private static final String SENTENCE = "I solemnly swear that I am up to no good.";

    @Test
    public void test() throws Throwable {
        // Send a random sentence to stdin.
        this.interactive.feedLine(SENTENCE);

        // Run the program and get the printed output.
        final String result = this.interactive.callMain().output();

        // Evaluate the result.
        Assert.assertEquals(SENTENCE, result);
    }
}
