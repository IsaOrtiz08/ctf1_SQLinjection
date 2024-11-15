This capture-the-flag is a simple SQL injection that accepts any input as the username, but the only acceptable passwords are "password123" or a successful sql injection sequence: ' OR '1' = '1

Either of these inputs will lead you to the page with the flag, the flag being flag{SQL_1nj3ct10n_success!}. If there is a different input, it will take you to an error screen saying please try logging in again.

This is my first time using Flask, so I am not sure how to deploy the project but all of the files are here.
