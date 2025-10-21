// 🌱 Hello World Plus Challenge
// Author: Vishwajeet Deshmane(https://github.com/o000SAI000o)
// Difficulty: Beginner
// Features: Interactive greeting, personalization, fun facts, motivational message

import java.util.*;
import java.time.*;
import java.time.format.DateTimeFormatter;

public class hello_world_plus_vishwajeet {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Hello World! Welcome to the Interactive Greeting Program! 🎉\n");

        // Ask for user's name
        System.out.print("What's your name? ");
        String name = sc.nextLine().trim();
        if (name.isEmpty()) {
            name = "Coder";
        }
        System.out.println("Nice to meet you, " + name + "! 👋\n");

        // Ask for favorite programming language
        System.out.print("What's your favorite programming language? ");
        String language = sc.nextLine().trim().toLowerCase();
        if (language.isEmpty()) {
            language = "python";
        }

        System.out.println("Excellent choice, " + name + "! " + capitalize(language) + " is awesome! 💻\n");

        // Show current date and time
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MMMM dd, yyyy, hh:mm a");
        String formattedDate = now.format(formatter);
        System.out.println("Today is: " + formattedDate + "\n");

        // Display fun fact
        String funFact = getFunFact(language);
        System.out.println("Fun Fact: " + funFact + "\n");

        // Display random motivational quote
        String quote = getRandomQuote();
        System.out.println("💬 Motivation: " + quote + "\n");

        // Closing message
        System.out.println("Thanks for joining our Student Fest Interactive Experience, " + name + "! 🌟");
        System.out.println("Keep coding and have a wonderful day! ✨");

        sc.close();
    }

    // Helper method: Capitalize first letter
    public static String capitalize(String str) {
        if (str == null || str.isEmpty()) return str;
        return str.substring(0, 1).toUpperCase() + str.substring(1);
    }

    // Helper method: Fun facts for languages
    public static String getFunFact(String language) {
        switch (language) {
            case "python":
                return "Did you know Python was named after the British comedy group Monty Python? 🎭";
            case "java":
                return "Java was originally called Oak, named after a tree outside James Gosling’s office! 🌳";
            case "c++":
                return "C++ was created as an extension of C to support object-oriented programming. 💡";
            case "javascript":
                return "JavaScript was developed in just 10 days by Brendan Eich at Netscape! ⚡";
            case "go":
                return "Go was created at Google to make coding fast and scalable. 🚀";
            case "rust":
                return "Rust focuses on performance and safety without a garbage collector. 🦀";
            default:
                return "Programming in " + capitalize(language) + " is a powerful skill! 🔥";
        }
    }

    // Helper method: Random motivational quote
    public static String getRandomQuote() {
        String[] quotes = {
            "Keep pushing your limits! 💪",
            "Every bug you fix makes you stronger. 🐞",
            "Code. Compile. Conquer. 🚀",
            "Dream in code and reality follows. ✨",
            "Debugging is like being a detective in a crime movie. 🔍"
        };
        Random rand = new Random();
        return quotes[rand.nextInt(quotes.length)];
    }
}
