<h1>Password checker using HaveIvBeenPwned API</h1>

An external file is read. File contains passwords.

First part of the password is cut of hashed and sent of to the API where the results witch have same hash are grouped en sent back.
Than the program cheks the responses but this time using the full hashed password. It returns if there are matches (compromises) of the password and how many there are.

<h2>What I learned</h2>

Using an external API. Interacting with it by following the documentation. 
Interacting wit the OS by reading a file with the given password list. 

<h2>This way the user can check his pass without the password leaving the computer.</h2> 

It returns the results in the terminal, but the password is partialy obscured. Also it shows the times the password appears in the compromised pass data base. The count of password cheked in one time is not limited.


Input txt file with passwords:

![Input txt of passwords](https://imgur.com/xEKftve.png)

Result in terminal:

![Terminal output](https://i.imgur.com/Ba8eWi9.png)
