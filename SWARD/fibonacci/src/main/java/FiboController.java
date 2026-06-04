import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Random;

@RestController
public class FiboController {

    private final Random random = new Random();

    @GetMapping(value = "/", produces = "text/plain")
    public String randomFibo() {
        int n = random.nextInt(10);
        return String.valueOf(Fibo.fibonacci(n));
    }
}