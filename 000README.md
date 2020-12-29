ZAWORLDOTHEBOT



*I use an .env file (who is hide by the repl.it IDE) for the token so you can just replace the "token" by your own token  



The @client.event() decorator is used to register an event. This is an asynchronous library, so things are done with callbacks. 
A callback is a function that is called when something else happens. 
In this code, the on_ready() event is called when the bot is ready to start being used.
Then, when the bot receives a message, the on_message() event is called.



the get_quote() uses the requests module to request data from the API URL.
The API returns a random inspirational quote. 
This function could easily be rewritten to get quotes from a different API, if the current one stops working.


Next inside the function, I use json.loads() to convert the response from the API to JSON. 
Through trial and error I figured out how to get the quote from the JSON into the string format I wanted. 
The quote is returned from the function as a string.

The final part updated in the code is toward the end. 
Previously it looked for a message that started with "$hello".
Now it looks for "$inspire".
Instead of returning "Hello!", it gets the quote with quote = get_quote() and returns the quote.
