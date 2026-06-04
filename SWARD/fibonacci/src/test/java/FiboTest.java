
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.beans.factory.annotation.Autowired;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest(
        classes = com.example.fibonacci.Application.class,
        webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT
)
public class FiboTest {

    @Autowired
    private TestRestTemplate restTemplate;

    @Test
    public void testHttpServerReturns200() {

        var response = restTemplate.getForEntity("/", Integer.class);

        assertEquals(200, response.getStatusCode().value());
    }
}