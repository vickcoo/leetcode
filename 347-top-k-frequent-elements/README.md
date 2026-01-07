## Approach

### Bucket Sort

First, calculate the frequency of each number to generate a hash map like the one below
```
input: [1, 1, 2, 2, 3, 4]
```
```
{
    1: 2,
    2: 2,
    3: 1,
    4: 1
}
```

Next, create an array called `bucket`, the index represents the **frequency** and the value stores the **number** that appear with that requency
| **Index / Frequency** | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Numbers** | [ ] | [3, 4] | [1, 2] | [ ] |

Finally, iterate through the array in reverse to retrieve the top `k` frequent numbers.
