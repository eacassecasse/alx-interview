# 0x06 - Star Wars API

## Overview
The "Star Wars Characters" project involves building a Node.js script that interacts with the Star Wars API to retrieve and display character names from a specified Star Wars movie. The script accepts a movie ID as a command-line argument and outputs each character's name in the order they appear in the movie's "characters" list.

## Requirements
### System Requirements
- **Operating System**: Ubuntu 20.04 LTS
- **Node.js**: Version 10.14.x
- **Editor**: Any standard editor, e.g., `vi`, `vim`, or `emacs`.

### General Requirements
- **File Format**:
  - Files should end with a newline.
  - The first line of each script should be `#!/usr/bin/node`.
  - Files must be executable.
  - Code should adhere to `semistandard` style, including semicolons.
- **Allowed Libraries**: Use of the `request` library for HTTP requests.
- **No `var` Usage**: Only `const` and `let` are allowed.

## Setup Instructions

1. **Install Node.js 10**
    ```bash
    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
    ```

2. **Install `semistandard` for Code Linting**
    ```bash
    $ sudo npm install semistandard --global
    ```

3. **Install the `request` Module**
    ```bash
    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules
    ```

## Key Concepts

To complete this project, understanding the following topics will be beneficial:

1. **HTTP Requests in JavaScript**:
   - Use `request` or `fetch` to make HTTP requests in Node.js.
   
2. **Working with APIs**:
   - Basics of RESTful APIs, interacting with JSON data, and parsing API responses.
   
3. **Asynchronous Programming**:
   - Managing asynchronous operations with callbacks, promises, and `async/await`.

4. **Command Line Arguments in Node.js**:
   - Access command-line arguments using `process.argv`.

5. **Array Manipulation and Iteration**:
   - Iterating and manipulating arrays to format and display character data.

## How to Use the Script

1. **Run the Script**:
   - The script expects a movie ID as an argument. Example:
     ```bash
     ./0-starwars_characters.js 3
     ```
   - The script will output character names line by line for the specified movie.

2. **Example Output**:
   ```bash
   $ ./0-starwars_characters.js 3
   Luke Skywalker
   C-3PO
   R2-D2
   Darth Vader
   Leia Organa
   Obi-Wan Kenobi
   Chewbacca
   Han Solo
   Jabba Desilijic Tiure
   ...
   ```

## Project Tasks

### Task 0: Star Wars Characters

Write a Node.js script that prints all characters of a Star Wars movie:
- The first argument is the movie ID (e.g., `3` for "Return of the Jedi").
- Display each character name on a new line in the same order as listed in the `/films/` endpoint.
- Use the Star Wars API (`https://swapi.dev/api/films/:id/`).
- Use the `request` module.

## Additional Resources
For further learning and technical practice:
- [HTTP Requests in Node.js](https://nodejs.org/en/docs/guides/)
- [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)
- [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Mock Technical Interview](https://www.example.com/mock-interview)

## License
This project is for educational purposes and follows the [MIT License](https://opensource.org/licenses/MIT).