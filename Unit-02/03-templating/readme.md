# Flask Templating

Create a new Flask application with the following:

- A `base.html` template for others to inherit from
- A route for `/person/<name>` 
- s
- s
- s
- s

### Bonus

Refactor your calculator application from before! 

- have a route for `/calculate` which renders a template called `calc.html`
- in `calc.html`, build a form which has two inputs for numbers and a select field with options for "add", "subract", "multiply" and "divide". 
- When the form is submitted it should make a request to a route called `/math`
- In your python file, accept the values from the form and depending on what the request contains, respond with the sum, difference, product or quotient.