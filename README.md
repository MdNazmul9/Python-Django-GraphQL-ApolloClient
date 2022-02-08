# Python-Django-GraphQL-ApolloClient

### query 1

```
{
  allIngredients {
    id
    name
  }
}
```

### query 2

```
query {
  categoryByName(name: "Dairy") {
    id
    name
    ingredients {
      id
      name
    }
  }
}
```

### query 3

```
query {
  allIngredients {
    id
    name
    category {
      id
      name
    }
  }
}
```

### query 4

```
query {
  allIngredients {
    edges {
      node {
        id,
        name
      }
    }
  }
}

# Output
{
  "data": {
    "allIngredient": {
      "edges": [
        {
          "node": {
            "id": "SW5ncmVkaWVudE5vZGU6MQ==",
            "name": "Eggs"
          }
        },
        {
          "node": {
            "id": "SW5ncmVkaWVudE5vZGU6Mg==",
            "name": "Milk"
          }
        },
        {
          "node": {
            "id": "SW5ncmVkaWVudE5vZGU6Mw==",
            "name": "Beef"
          }
        },
        {
          "node": {
            "id": "SW5ncmVkaWVudE5vZGU6NA==",
            "name": "Chicken"
          }
        }
      ]
    }
  }
}

```

### query 5

```
query {
  allCategories {
    edges {
      node {
        name,
        ingredients {
          edges {
            node {
              name
            }
          }
        }
      }
    }
  }
}

# output

{
  "data": {
    "allCategories": {
      "edges": [
        {
          "node": {
            "name": "Dairy",
            "ingredients": {
              "edges": [
                {
                  "node": {
                    "name": "Eggs"
                  }
                },
                {
                  "node": {
                    "name": "Milk"
                  }
                }
              ]
            }
          }
        },
        {
          "node": {
            "name": "Meat",
            "ingredients": {
              "edges": [
                {
                  "node": {
                    "name": "Beef"
                  }
                },
                {
                  "node": {
                    "name": "Chicken"
                  }
                }
              ]
            }
          }
        }
      ]
    }
  }
}

```

### query 6
```
query {
  # You can also use `category: "CATEGORY GLOBAL ID"`
  allIngredients(name_Icontains: "e", category_Name: "Meat") {
    edges {
      node {
        name
      }
    }
  }
}

# or 
query{
  allIngredient(name_Icontains: "e", category_Name: "Dairy"){
    edges{
      node{
        name
      }
    }
  }
}

# Output
{
  "data": {
    "allIngredient": {
      "edges": [
        {
          "node": {
            "name": "Eggs"
          }
        }
      ]
    }
  }

```