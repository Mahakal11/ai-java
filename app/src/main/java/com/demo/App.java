package com.demo;

public class App {

    public static void main(String[] args) {

        System.out.println("Hello World!");

    }

}package com.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@RestController
public class App {

    @GetMapping("/cpu")
    public String cpuSpike() {
        while (true) {} // ❌ Intentional CPU bug for AI detection
    }

    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}
