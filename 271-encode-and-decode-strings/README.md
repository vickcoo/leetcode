## Approach

### Length-Prefixed Encoding

The key insight is to use a **length-prefix format** where each string is encoded as `{length}#{string}`. The `#` character acts as a delimiter between the length and the actual string content.

#### Encoding Process

For each string in the input array, prepend its length followed by a `#` delimiter:

```
Input: ["Hello", "World"]
Output: "5#Hello5#World"
```

This format handles edge cases like:
- Empty strings: `["", "a"]` → `"0#1#a"`
- Strings containing special characters: `["a#b", "c"]` → `"3#a#b1#c"`

#### Decoding Process

Parse the encoded string by:
1. Read characters until we find `#` to get the length
2. Extract the substring of that exact length after `#`
3. Move the pointer forward by `length + 1` (for the `#`)
4. Repeat until the end of the string

**Example walkthrough:**
```
Encoded: "5#Hello5#World"

Step 1: Read "5" → length = 5
        Extract "Hello" (5 characters after #)

Step 2: Read "5" → length = 5
        Extract "World" (5 characters after #)

Result: ["Hello", "World"]
```

**Time Complexity:** O(n) for both encode and decode, where n is the total length of all strings
**Space Complexity:** O(1) excluding the output