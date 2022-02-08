# Python-Django-GraphQL-ApolloClient

# query 1
```
{
  allIngrediants {
    id
    name
  }
}
```

# query 2
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

# query 3
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