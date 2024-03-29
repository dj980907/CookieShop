# Cookie Shop

This is a virtual cookie shop where users can order all kinds of cookies!

## Cookie inventory

The cookie shop has an inventory of at least **10 different kinds of cookies**. 
A data file named `cookies.csv` contains id, name, description, and price associated with each cookie.
Each cookie is also marked as to whether it is `sugar free`, `gluten free`, or `contains nuts` for those with diabetes or allergies. 

## Welcome message

Running the program first shows a welcome message.

```
Welcome to the Python Cookie Shop!
We feed each according to their need.
```

The welcome message additionally asks the user questions whether they have any allergies to nuts or gluten, and whether they are avoiding sugar.

Here is sample of the additional output for this version, including example responses from the user.

```
We'd hate to trigger an allergic reaction in your body. So please answer the following questions:

Are you allergic to nuts? yes
Are you allergic to gluten? no
Do you suffer from diabetes? yes
```

## List of cookies

The program then outputs a user-friendly list of the cookies in the shop.
Rather than showing all the cookies in the store, it outputs a user-friendly list of only those cookies that match the user's dietary needs.

For example, a user with a gluten allergy should be shown only those cookies without gluten. And likewise for sugar and nuts.

Sample output below:

```
Great! Here are the cookies without nuts or sugar that we think you might like:

#1 - Basboosa Semolina Cake
This is a traditional Middle Eastern dessert made with semolina and yogurt, then soaked in a rose water syrup.
Price: $3.99

#4 - Animal Cupcake
Go wild and choose from a set of animal faces or one animal face printed on edible sugar paper.
Price: $0.99
```

## Taking orders

The user is then asked to enter the `id` number of any cookie he/she would like to purchase, as well as the quantity. The user must enter the number of the cookie and the quantity as integers (e.g. `4`).

Sample output, including example responses from the user:

```
Please enter the number of any cookie you would like to purchase: 4
My favorite! How many Animal Cupcakes would you like? 8
Your subtotal for 8 Animal Cupcakes is $7.92.
```

The user is prompted over-and-over to enter the `id` number of any aadditional cookie they would like to purchase until they type '`finished`'.

When the ordering is finished, the total price is displayed.

```
Please enter the number of any other cookie you would like to purchase (type "finished" if finished with your order): finished

Thank you for your order. You have ordered:

-8 Animal Cupcake
-1 Basboosa Semolina Cake

Your total is $11.91.
Please pay with Bitcoin before picking-up.

Thank you!
-The Python Cookie Shop Robot.
```

## Parsing the data file

Except for the first line, which contains field headings, each line in the `cookies.csv` data file contains information about one cookie. The program must read the data from this file once at the beginning of running the program, and store the data found in the file into the appropriate data structures in the memory of the program.

## One dictionary per cookie

The data for each cookie must be stored as a dictionary. The dictionary must have keys for `id`, `title`, `description`, and `price`.

- The value of '`id`' must be an Integer.
- The value of '`title`' must be a String.
- The value of '`description`' must be a String.
- The value of '`price`' must be a Float with two decimal points.
- The dictionary must also have additional keys for '`sugar_free`', '`gluten_free`', and '`contains_nuts`'. Each should have a boolean value associated with it.
  
For example, here is what a dictionary with data for one cookie would look like, if the values were written as literals in the code, rather than pulled from the data file:

```python
{
  'id': 1,
  'title': 'Basboosa Semolina Cake',
  'description': "This is a This is a traditional Middle Eastern dessert made with semolina and yogurt, then soaked in a rose water syrup.",
  'price': 3.99
}
```

## Dictionaries stored in a list

All dictionaries representing individual cookies must be stored together as elements in a list. In other words, there is a single list that contains all the 10 or more cookie dictionaries.

```python
[
  {
    'id': 1,
    'title': 'Basboosa Semolina Cake',
    'description': "This is a This is a traditional Middle Eastern dessert made with semolina and yogurt, then soaked in a rose water syrup.",
    'price': 3.99
  },
  {
    'id': 2,
    'title': 'Vanilla Chai Cookie',
    'description': "Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner, a combination of cinnamon, ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?",
    'price': 5.50
  },
  # and so on...
]
```

## User input validation

All user input data must be validated. If the user enters inappropriate data, the program must response by repeating the request for input. Data to validate includes:

- The `id` number of the cookie the user would like to order must be entered as an integer (e.g. `4`). This integer must be an actual `id` for a cookie in the cookie shop.
- The quantity of an ordered cookie must be an integer.
- The words '`finished`', '`done`', '`quit`', or '`exit`' in response to the request for the user to enter an additional cookie `id` must trigger the program to stop asking the user for more orders and continue to show them the total price for their order.
