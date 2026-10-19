import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class EchoTest {
    private static final String SENTENCE = "I solemnly swear that I am up to no good.";

    private final InputStream originalIn = System.in;
    private final PrintStream originalOut = System.out;
    private final ByteArrayOutputStream output = new ByteArrayOutputStream();

    @Before
    public void redirectStreams() {
        System.setIn(new ByteArrayInputStream((SENTENCE + "\n").getBytes(StandardCharsets.UTF_8)));
        System.setOut(new PrintStream(output, true, StandardCharsets.UTF_8));
    }

    @After
    public void restoreStreams() {
        System.setIn(originalIn);
        System.setOut(originalOut);
    }

    @Test
    public void test() {
        Echo.main(new String[0]);

        Assert.assertEquals(SENTENCE, output.toString(StandardCharsets.UTF_8).trim());
    }
}
