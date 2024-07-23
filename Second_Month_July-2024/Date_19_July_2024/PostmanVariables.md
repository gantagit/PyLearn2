Sure! Here's a breakdown of the different types of variables in Postman and examples for each:

### Global Variables
Global variables are accessible throughout the entire workspace, making them useful for values that need to be reused across multiple collections and environments.

**Example:**
1. Go to the **Environment Quick Look** icon (eye icon) in the top right corner.
2. Click on **Globals** and then **Edit**.
3. Add a variable named `base_url` with the value `https://api.example.com`.
4. Use `{{base_url}}` in your requests, e.g., `{{base_url}}/users`.

### Collection Variables
Collection variables are specific to a collection and can be used within any request in that collection.

**Example:**
1. Open the collection and click on the **Variables** tab.
2. Add a variable named `api_key` with the value `12345`.
3. Use `{{api_key}}` in your requests, e.g., `{{api_key}}` in the headers.

### Variables within the Script
These variables are defined and used within the pre-request or test scripts. They are not accessible outside the script they are defined in.

**Example:**
```javascript
// Pre-request Script
pm.variables.set("token", "abcdef12345");

// Test Script
let token = pm.variables.get("token");
console.log(token); // Outputs: abcdef12345
```

### Environment Variables
Environment variables are tied to a specific environment and can be switched based on the context (e.g., development, staging, production).

**Example:**
1. Create an environment by clicking on the **Environment Quick Look** icon and then **Add**.
2. Name the environment (e.g., Development) and add a variable named `host` with the value `dev.api.example.com`.
3. Use `{{host}}` in your requests, e.g., `https://{{host}}/users`.

These variables help make your API requests more dynamic and reusable, allowing you to easily switch contexts and manage different configurations¹².

Do you need more details on any specific type of variable?

Source: Conversation with Copilot, 23/07/2024
(1) Store and reuse values using variables | Postman Learning Center. https://learning.postman.com/docs/sending-requests/variables/variables/.
(2) Reuse data with variables and environments in Postman. https://learning.postman.com/docs/sending-requests/variables/variables-intro/.
(3) Configuring variables and environments - Postman. https://academy.postman.com/working-with-variables-and-environments.
(4) Loops and Dynamic Variables in Postman: Part 1 - Medium. https://medium.com/@cantrobot/loops-and-dynamic-variables-in-postman-part-1-36cc6cfb2964.
(5) undefined. https://postman-echo.com.
(6) undefined. https://postman-echo.com/get.
(7) undefined. https://postman-echo.com/get?var=.
(8) How to create and use global variables in Postman?. https://www.geeksforgeeks.org/how-to-create-and-use-global-variables-in-postman/.
(9) A Guide to Variables in Postman | Baeldung. https://www.baeldung.com/java-postman-variables.
(10) Difference between global and local variables in Postman. https://www.geeksforgeeks.org/difference-between-global-and-local-variables-in-postman/.
(11) undefined. https://jsonplaceholder.typicode.com/posts/?userId=.
(12) en.wikipedia.org. https://en.wikipedia.org/wiki/Postman_(software).